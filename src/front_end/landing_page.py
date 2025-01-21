# landing page for the app

import flet as ft
from PIL import Image
from front_end.config.settings import LANDING_PAGE_CONFIG

def landing_page(page: ft.Page, navigate_to):
    
    page.scroll = LANDING_PAGE_CONFIG["scroll"]
    config = LANDING_PAGE_CONFIG
    images = config["images"]
    texts = config["texts"]
    sizes = config["sizes"]
    colors = config["colors"]

    def route_to_home(e):
        from front_end.home_page import home_page
        navigate_to(lambda p: home_page(p, navigate_to))

    def get_dynamic_size(page, img_path, fit_type="cover"):
        # calculates dynamic image size to fit the app's dimensions based on the fit type.

        with Image.open(img_path) as img:
            img_width, img_height = img.size

        app_width, app_height = page.width, page.height
        img_aspect_ratio = img_width / img_height
        app_aspect_ratio = app_width / app_height

        if fit_type == "cover":
            if img_aspect_ratio > app_aspect_ratio:
                scaled_height = app_height
                scaled_width = int(scaled_height * img_aspect_ratio)
            else:
                scaled_width = app_width
                scaled_height = int(scaled_width / img_aspect_ratio)

        elif fit_type == "contain":
            if img_aspect_ratio > app_aspect_ratio:
                scaled_width = app_width
                scaled_height = int(scaled_width / img_aspect_ratio)
            else:
                scaled_height = app_height
                scaled_width = int(scaled_height * img_aspect_ratio)

        return scaled_width, scaled_height
    
    # builds the landing page content
    page.add(
        ft.Stack(
            controls=[
                # background image (Layer -2)
                ft.Image(
                    src=images["background_image"],
                    fit=ft.ImageFit.COVER,
                    width=get_dynamic_size(page, images["background_image"], "cover")[0],
                    height=get_dynamic_size(page, images["background_image"], "cover")[1],
                ),
                # top image (Layer -1)
                ft.Image(
                    src=images["top_image"],
                    fit=ft.ImageFit.COVER,
                    width=get_dynamic_size(page, images["top_image"], "cover")[0],
                    height=get_dynamic_size(page, images["top_image"], "contain")[1],
                ),
                # foreground content (Layer 0)
                ft.Column(
                    [
                        # top Section
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Image(
                                        src=images["logo_image"],
                                        width=sizes["logo_size"],
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text(
                                                texts["title_lines"][0],
                                                size=sizes["title_font_size"],
                                                weight=ft.FontWeight.W_700,
                                                color=colors["title_color"][0],
                                                text_align=ft.TextAlign.LEFT,
                                            ),
                                            ft.Text(
                                                texts["title_lines"][1],
                                                size=sizes["title_font_size"],
                                                weight=ft.FontWeight.W_700,
                                                color=colors["title_color"][1],
                                                text_align=ft.TextAlign.LEFT,
                                            ),
                                        ],
                                        spacing=0,
                                        horizontal_alignment=ft.CrossAxisAlignment.START,
                                    ),
                                    ft.Text(
                                        texts["subtitle"],
                                        size=sizes["subtitle_font_size"],
                                        weight=ft.FontWeight.W_400,
                                        color=colors["subtitle_color"],
                                        text_align=ft.TextAlign.LEFT,
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                spacing=2,
                            ),
                            padding=ft.padding.all(24),
                            alignment=ft.alignment.center_left,
                        ),
                        # bottom Section
                        ft.Container(
                            content=ft.ElevatedButton(
                                text=texts["button_text"],
                                style=ft.ButtonStyle(
                                    bgcolor=colors["button_background_color"],
                                    color=colors["button_text_color"],
                                    shape=ft.RoundedRectangleBorder(
                                        radius=sizes["button_radius"]
                                    ),
                                    side=ft.BorderSide(
                                        color=colors["button_stroke_color"],
                                        width=sizes["button_border_width"],
                                    ),
                                    padding=ft.padding.all(0),
                                    text_style=ft.TextStyle(
                                        size=sizes["button_font_size"]
                                    ),
                                ),
                                width=sizes["button_width"],
                                height=sizes["button_height"],
                                on_click=route_to_home,
                            ),
                            alignment=ft.alignment.bottom_center,
                            padding=ft.padding.only(
                                bottom=sizes["button_bottom_spacing"]
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    expand=False,
                ),
            ],
            expand=True,
        )
    )
