# image analysis
# returns series of image data to be passed onto prediction models

import flet as ft
import cv2, base64, threading, time, requests, json
import numpy as np
from typing import List, Dict, Tuple

from back_end.crop_info import CropInfo
from back_end.geolocation import GeoLocation
from back_end.config.settings import CROP_DETECTION_APIS

class Camera:
    def __init__(self):
        self.camera = None
        self.is_camera_running = threading.Event()
        self.captured_images: List[Tuple] = []  # for storing images in format (frame, (latitude, longitude))
        self.geolocator = GeoLocation()

    def start_camera(self):
        # iinitializes the camera
        self.camera = cv2.VideoCapture(0)

    def stop_camera(self):
        # releases the camera resource
        if self.camera:
            self.camera.release()
            self.camera = None

    def show_camera(self, live_image: ft.Page):
        # starts displaying the live feed from the camera
        # arg. live_image: Flet Image control to display the feed
        if self.camera is None:
            self.start_camera()

        self.is_camera_running.set()

        def update_live_feed():
            while self.is_camera_running.is_set():
                ret, frame = self.camera.read()
                if ret:
                    _, buffer = cv2.imencode(".jpg", frame)
                    img_data = base64.b64encode(buffer).decode("utf-8")
                    live_image.src_base64 = img_data
                    live_image.update()
                time.sleep(0.03)

        # starts the live feed update in a thread
        feed_thread = threading.Thread(target=update_live_feed, daemon=True)
        feed_thread.start()

    def stop_live_feed(self):
        # stops the live feed
        self.is_camera_running.clear()

    def capture_single_photo(self):
        # captures a single photo from the camera
        if self.camera is None:
            return None
        ret, frame = self.camera.read()
        self._append_frame(ret, frame)
        self.stop_live_feed()
        self.stop_camera()

    def capture_multiple_photos(self):
        # captures a photo and append it to the list of captured images
        if self.camera is None:
            self.start_camera()
        ret, frame = self.camera.read()
        self._append_frame(ret, frame)
    
    def _append_frame(self, ret, frame):
        # append to captured_images list with geolocation data
        if ret:
            try:
                latitude, longitude = self.geolocator.get_current_location()
                self.captured_images.append((frame, (latitude, longitude)))
            except Exception as e:
                print("Failed to fetch geolocation:", str(e))
                self.captured_images.append((frame, None))

    def get_captured_images(self):
        # retrieves all captured images and clear the list
        # return: List of captured images
        captured = self.captured_images.copy()
        self.captured_images.clear()
        self.stop_live_feed()
        self.stop_camera()
        return captured
    


class ImageProcessing:
    def __init__(self):
        # initializes the ImageProcessing class with API configurations
        self.api_details = CROP_DETECTION_APIS
    
    def _detect_crops(self, image: np.ndarray, latitude: float, longitude: float, api_index: int = 0) -> List[Dict]:
        # detects crops in an image using the specified API and returns the detection results
        # arg. image: input image as a NumPy array
        # arg. latitude: latitude of current location
        # arg. longitude: longitude of current location
        # arg. api_index: index of the API configuration to use
        # return: response from api in json format
        if api_index >= len(self.api_details):
            raise ValueError("Invalid API index provided.")

        api_config = self.api_details[api_index]
        
        # converts the image to base64 encoding
        _, encoded_image = cv2.imencode('.jpg', image)
        image_base64 = base64.b64encode(encoded_image).decode('utf-8')

        # prepares the payload in json
        payload = json.dumps({
            "images": [image_base64],
            "latitude": latitude,
            "longitude": longitude,
            "similar_images": True
        })

        # defines the headers of the api
        headers = {
            "Api-Key": api_config["api_key"],
            "Content-Type": "application/json"
        }

        # makes the request for response
        response = requests.post(
            url=api_config["api_url"],
            headers=headers,
            data=payload
        )

        if response.status_code not in (200, 201):
            raise Exception(f"API request failed: {response.status_code}, {response.text}")

        # tries to convert response to json format 
        try:
            response_in_json = response.json()
        except ValueError:
            raise Exception(f"Invalid JSON response: {response.text}")
        return response_in_json

    def process_local_images(self, images: List[Tuple[np.ndarray, Tuple[float, float]]], api_index: int = 0) -> Dict:
        # processes a local image to detect and return cropped images of the top crop type
        # arg. images: list of images and their geolocation data
        # arg. api_index: index of the API configuration to use
        # return: the complete json for the prediction with the highest probability
        all_predictions = []

        # processes each image
        for image, location in images:
            latitude, longitude = location
            predictions = self._detect_crops(image, latitude, longitude, api_index)
            all_predictions.append(dict(predictions))

        crop_info = CropInfo()
        highest_probability_prediction = crop_info.get_top_prediction(all_predictions)

        return highest_probability_prediction if highest_probability_prediction else {}