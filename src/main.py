# main entry point for the application
# this script should start displaying the app when the command runs
# cmd: flet run

import flet as ft
from front_end.config.settings import MAIN_CONFIG

def main(page: ft.Page):
    
    page.title = MAIN_CONFIG["title"]
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = MAIN_CONFIG["scroll"]
    page.window.width = MAIN_CONFIG["default_width"]
    page.window.height = MAIN_CONFIG["default_height"]
    
    page.fonts = {
        "SF Pro Display": "./src/assets/fonts/sf_pro_display_regular.OTF"
    }
    page.theme = ft.Theme(font_family="SF Pro Display")

    # navigates to a specific page
    def navigate_to(page_content):
        page.clean()
        page_content(page)
        page.update()

    # displays landing page initially
    from front_end.landing_page import landing_page
    navigate_to(lambda p: landing_page(p, navigate_to))

ft.app(target=main)
