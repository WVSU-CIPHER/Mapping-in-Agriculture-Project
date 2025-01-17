import flet as ft

from back_end.image_processing import Camera, ImageProcessing
from back_end.crop_info import CropInfo

def main(page: ft.Page):
    # page information of the app
    page.title = "Crop Detection App"
    page.window.width = 360
    page.window.height = 640
    page.scroll = "adaptive"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # initializing systems to be used for crop analyzing
    image_processor = ImageProcessing()
    camera = Camera()

    def single_capture():
        # displays view of single capture
        live_image = ft.Image(width=320, height=240)    # to be utilized for live feed display
        camera.show_camera(live_image)

        def capture_photo(_):
            # captures the current video feed
            # calls by on_click button
            camera.capture_single_photo()
            result = image_processor.process_local_images(camera.get_captured_images())
            results_view(result)

        single_camera_view = ft.View(
            "/single",
            [
                ft.Text("Single Capture Mode", size=24, weight="bold"),
                live_image,
                ft.ElevatedButton("Capture", on_click=capture_photo),
                ft.ElevatedButton("Go Back", on_click=go_back),
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        page.views.append(single_camera_view)
        page.update()

    def multiple_capture():
        # displays view of multiple capture
        live_image = ft.Image(width=320, height=240)    # to be utilized for live feed display
        camera.show_camera(live_image)
        status_text = ft.Text(value="No images captured yet.")

        def capture_photo(_):
            # captures the current video feed and add one to the list
            # calls by on_click button
            camera.capture_multiple_photos()
            status_text.value = f"Captured {len(camera.captured_images)} image(s)"
            status_text.update()

        def done_capturing(_):
            # processes all listed images captured
            # calls by on_click button
            result = image_processor.process_local_images(camera.get_captured_images())
            results_view(result)

        multiple_camera_view = ft.View(
            "/multiple",
            [
                ft.Text("Multiple Capture Mode", size=24, weight="bold"),
                live_image,
                status_text,
                ft.Row(
                    [
                        ft.ElevatedButton("Capture", on_click=capture_photo),
                        ft.ElevatedButton("Done", on_click=done_capturing),
                    ]
                ),
                ft.ElevatedButton("Go Back", on_click=go_back),
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        page.views.append(multiple_camera_view)
        page.update()

    def results_view(result):
        # displays the information and results
        crop_name = CropInfo.get_top_crop_name(result)
        scientific_disease_name = CropInfo.get_top_disease_name(result, True)

        results_text = f"Crop Found!\n   Crop Name: {crop_name}\n   Disease Name: {scientific_disease_name}"
        results_view = ft.View(
            "/results",
            [
                ft.Text("Detection Results", size=24, weight="bold"),
                ft.Text(results_text),
                ft.ElevatedButton("Go Back", on_click=go_back),
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        page.views.append(results_view)
        page.update()

    def go_back(_):
        # go back to main menu
        show_main_menu()
        page.update()

    def show_main_menu():
        # displays the main menu
        main_menu_view = ft.View(
            "/",
            [
                ft.Text("Crop Detection App", size=24, weight="bold"),
                ft.ElevatedButton("Single Capture", on_click=lambda _: single_capture()),
                ft.ElevatedButton("Multiple Capture", on_click=lambda _: multiple_capture()),
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        page.views.append(main_menu_view)
        page.update()

    show_main_menu()

ft.app(target=main)