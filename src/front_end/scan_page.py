# scan page for the app

import flet as ft
from front_end.config.settings import SCAN_PAGE_CONFIG
from back_end.image_processing import Camera, ImageProcessing
from back_end.crop_info import CropInfo
from back_end.geolocation import GeoLocation
from back_end.predictions.weather_impact_estimation import CropWeatherImpact
from back_end.predictions.disease_risk_prediction import CropDiseaseRisk
from back_end.predictions.success_rate_prediction import CropSuccessRate
from back_end.predictions.suggestion_guess import CropSuggestion
from back_end.database import Database

def scan_page(page: ft.Page, navigate_to):
    
    config = SCAN_PAGE_CONFIG
    images = config["images"]
    colors = config["colors"]
    
    image_processor = ImageProcessing()
    camera = Camera()
    live_preview = None

    def initialize_camera():
        global live_preview
        live_preview = ft.Image(
            fit=ft.ImageFit.COVER,
        )
        camera.show_camera(live_preview)
        return live_preview
    
    def capture_photo(e):
        camera.capture_single_photo()
        result = image_processor.process_local_images(camera.get_captured_images())
        process_result(result)

    def route_to_home(e):
        camera.stop_camera()
        from front_end.analysis_page import analysis_page
        navigate_to(lambda p: analysis_page(p, navigate_to))

    # Layout structure
    page.add(
        ft.Container(
            bgcolor=colors["body_color"],
            content=ft.Column([
                # Header with back button
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            content=ft.Image(
                                src=images["back_icon"],
                            ),
                            on_click=route_to_home,
                            style=ft.ButtonStyle(
                                bgcolor={"": ft.colors.TRANSPARENT},
                                padding=0,
                            ),
                        ),
                    ]),
                    margin=ft.margin.only(left=10,top=10),
                ),

                # Image preview
                ft.Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(left=20, right=20, top=20),
                    height=360,
                    border_radius=10,
                    bgcolor=colors["camera_background"],
                    content=initialize_camera(),
                ),

                # Capture button
                ft.Container(
                    content=ft.IconButton(
                        content=ft.Image(
                            src=images["capture_icon"],
                        ),
                        on_click=capture_photo,
                        style=ft.ButtonStyle(
                            shape=ft.CircleBorder(),
                            padding=20,
                        ),
                    ),
                    alignment=ft.alignment.bottom_center,
                    padding=ft.padding.only(
                        bottom=20,
                    ),
                ),
            ]),
            expand=True,
        )
    )

    def process_result(result):
        crop_info = CropInfo()
        geolocation = GeoLocation()
        geo_latitude, geo_longitude = geolocation.get_current_location()

        crop_name = crop_info.get_top_crop_name(result)
        disease_name = crop_info.get_top_disease_name(result, True)
        image_url = crop_info.get_image_url(result)
        
        symptoms = crop_info.get_all_disease_symptoms(result)
        severity = crop_info.get_disease_severity(result)
        spreading = crop_info.get_disease_spreading(result)
        preventions = crop_info.get_all_prevention_treatment(result)
        chemical_treatment = crop_info.get_all_chemical_treatment(result)
        biological_treatment = crop_info.get_all_biological_treatment(result)

        crop_details_for_disease_risk = {
            "crop_name": crop_name,
            "disease_name": disease_name,
            "symptoms": symptoms,
            "severity": severity,
            "spreading": spreading,
        }

        crop_disease_risk = CropDiseaseRisk()
        disease_risk_value, disease_risk_reasoning = crop_disease_risk.get_risk_value(**crop_details_for_disease_risk)
        disease_risk_level = crop_disease_risk.get_risk_indicator_level(disease_risk_value)

        crop_weather_impact = CropWeatherImpact()
        crop_weather_impact.fetch_weather_data(geo_latitude, geo_longitude)

        day_index = 0
        geo_elevation = crop_weather_impact.get_elevation()
        weather_temperature = crop_weather_impact.get_temperature(day_index)
        weather_temperature_risk_level = crop_weather_impact.get_temperature_risk_level(day_index)
        weather_precipitation = crop_weather_impact.get_precipitation(day_index)
        weather_precipitation_risk_level = crop_weather_impact.get_precipitation_risk_level(day_index)
        weather_wind_speed = crop_weather_impact.get_wind_speed(day_index)
        weather_wind_speed_risk_level = crop_weather_impact.get_wind_speed_risk_level(day_index)
        weather_overall_risk_level = crop_weather_impact.get_overall_risk(day_index)

        crop_details_for_success_rate = {
            "crop_name": crop_name,
            "latitude": geo_latitude,
            "elevation": geo_elevation,
            "weather_temperature": weather_temperature,
            "weather_precipitation": weather_precipitation,
            "weather_wind_speed": weather_wind_speed,
            "disease_risk_value": disease_risk_value
        }

        crop_success_rate = CropSuccessRate()
        success_rate_value = crop_success_rate.calculate_success_rate(**crop_details_for_success_rate)

        crop_details_for_suggestion_guess = {
            "crop_name": crop_name,
            "disease_name": disease_name,
            "success_rate": success_rate_value,
            "weather_risks": {
                "temperature_risk": weather_temperature_risk_level, 
                "precipitation_risk": weather_precipitation_risk_level, 
                "wind_speed_risk": weather_wind_speed_risk_level,
            },
            "disease_risks": {
                "symptoms": symptoms,
                "severity": severity, 
                "spread": spreading,
            },
            "treatments": {
                "preventions": preventions,
                "chemical_treatment": chemical_treatment,
                "biological_treatment": biological_treatment,
            },
        }

        crop_suggestion = CropSuggestion()
        suggestions = crop_suggestion.get_suggestions(**crop_details_for_suggestion_guess)

        date, time = crop_info.get_datetime(result)
        crop_data_for_saving = {
            "crop_name": crop_name,
            "image_url": image_url,
            "coordinate": {
                "latitude": geo_latitude,
                "longitude": geo_longitude,
                "elevation": geo_elevation,
            },
            "disease_risks": {
                "disease_name": disease_name,
                "symptoms": symptoms,
                "severity": severity,
                "spreading": spreading,
            },
            "treatments": {
                "preventions": preventions,
                "chemical_treatment": chemical_treatment,
                "biological_treatment": biological_treatment,
            },
            "prediction": {
                "success_rate": success_rate_value,
                "weather_impact": {
                    "temperature": weather_temperature,
                    "temperature_risk_level": weather_temperature_risk_level,
                    "precipitation": weather_precipitation,
                    "precipitation_risk_level": weather_precipitation_risk_level,
                    "wind_speed": weather_wind_speed,
                    "wind_speed_risk_level": weather_wind_speed_risk_level,
                    "overall_risk_level": weather_overall_risk_level,
                },
                "disease_impact": {
                    "value": disease_risk_value,
                    "risk_level": disease_risk_level,
                },
                "suggestions": suggestions,
            },
        }
        
        database = Database()
        database.save_data(date, time, crop_data_for_saving)

        from front_end.analysis_page import analysis_page
        navigate_to(lambda p: analysis_page(p, navigate_to))