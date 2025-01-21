# home page for the app

import flet as ft
from front_end.config.settings import HOME_PAGE_CONFIG
from back_end.geolocation import GeoLocation, DateTime
from back_end.weather_info import WeatherInfo
from back_end.database import Database

def home_page(page: ft.Page, navigate_to):
    
    page.scroll = HOME_PAGE_CONFIG["scroll"]
    config = HOME_PAGE_CONFIG
    images = config["images"]
    sizes = config["sizes"]
    colors = config["colors"]

    datetime = DateTime()
    geolocation = GeoLocation()
    geo_latitude, geo_longitude = geolocation.get_current_location()
    weather_info = WeatherInfo()
    weather_info.fetch_weather_data(geo_latitude, geo_longitude)
    database = Database()
    max_count_data = config["display_count_data"]
    latest_data, count_data = database.load_data(max_count_data)

    def route_to_home(e):
        pass
        
    def route_to_analytics(e):
        from front_end.analysis_page import analysis_page
        navigate_to(lambda p: analysis_page(p, navigate_to))
        
    def route_to_camera(e):
        pass
        
    def route_to_logs(e):
        pass
        
    def route_to_profile(e):
        pass

    # header section
    header = ft.Container(
        bgcolor=colors["body_color"],
        content=ft.Column(
            [
                # general information
                ft.Container(
                    content=ft.Row([
                        ft.Column(
                            alignment=ft.alignment.center_left,
                            spacing=0,
                            controls=[
                                ft.Text(
                                    "Hello, Farmer!", 
                                    size=sizes["large_text"],
                                    weight=ft.FontWeight.BOLD, 
                                    color=colors["header_text_color"]
                                ),
                                ft.Text(
                                    f"{datetime.get_current_weekday()}, {datetime.get_current_day()}", 
                                    size=sizes["medium_text"], 
                                    color=colors["header_text_color"]
                                ),
                            ],
                        ),
                        ft.Column(
                            alignment=ft.alignment.center_right,
                            spacing=0,
                            expand=True,
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.END,
                                    spacing=0,
                                    controls=[
                                        ft.Image(src=images["weather_icon"]),
                                        ft.Text(
                                            f"{weather_info.get_temperature()}°C", 
                                            size=sizes["medium_text"], 
                                            color=colors["header_text_color"]
                                        ),
                                    ],
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.END,
                                    spacing=2,
                                    controls=[
                                        ft.Image(src=images["location_icon"]),
                                        ft.Text(
                                            f"{geolocation.get_address_from_coordinates(geo_latitude, geo_longitude)}", 
                                            size=sizes["extra_small_text"], 
                                            color=colors["header_text_color"]
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ]),
                    padding=ft.padding.all(20),
                    bgcolor=colors["header_color"],
                    border_radius=ft.border_radius.only(bottom_left=60, bottom_right=60),
                    height=130
                ),
                
                # weather information
                ft.Container(
                    margin=ft.margin.only(top=-40,bottom=10,left=20,right=20),
                    padding=ft.padding.all(10),
                    bgcolor=colors["weather_container_color"],
                    border_radius=8,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=2,
                        color=ft.colors.GREY_400,
                        offset=ft.Offset(0, 2)
                    ),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Image(src=images["heat_index_icon"]),
                                    ft.Text(
                                        f"{weather_info.get_heat_index()}°C", 
                                        size=sizes["small_text"],
                                        color=colors["weather_info_data_color"],
                                    ),
                                    ft.Text("Heat Index", size=sizes["extra_small_text"], color=colors["weather_info_name_color"]),
                                ]
                            ),
                            ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Image(src=images["humidity_icon"]),
                                    ft.Text(
                                        f"{weather_info.get_humidity()}%", 
                                        size=sizes["small_text"],
                                        color=colors["weather_info_data_color"],
                                    ),
                                    ft.Text("Humidity", size=sizes["extra_small_text"], color=colors["weather_info_name_color"]),
                                ]
                            ),
                            ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Image(src=images["precipitation_icon"]),
                                    ft.Text(
                                        f"{weather_info.get_rainfall()} mm", 
                                        size=sizes["small_text"],
                                        color=colors["weather_info_data_color"],
                                    ),
                                    ft.Text("Rainfall", size=sizes["extra_small_text"], color=colors["weather_info_name_color"]),
                                ]
                            ),
                            ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Image(src=images["wind_speed_icon"]),
                                    ft.Text(
                                        f"{weather_info.get_wind_speed()} m/s", 
                                        size=sizes["small_text"],
                                        color=colors["weather_info_data_color"],
                                    ),
                                    ft.Text("Wind Speed", size=sizes["extra_small_text"], color=colors["weather_info_name_color"]),
                                ]
                            ),
                        ],
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )

    # body section
    body = ft.Container(
        bgcolor=colors["body_color"],
        content=ft.Column(
            controls=[
                ft.Text("Farm List", size=sizes["medium_text"], weight=ft.FontWeight.BOLD, color=colors["body_title_color"]),
                ft.ListView(
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(
                                            src="src/assets/landing_background_image.png",
                                            width=80,
                                            height=80,
                                            fit=ft.ImageFit.COVER,
                                        ),
                                        width=80,
                                        height=80,
                                        border_radius=8,
                                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                    ),
                                    ft.Column(
                                        expand=True,
                                        controls=[
                                            ft.Column(
                                                spacing=0,
                                                controls=[
                                                    ft.Text(f"Farm Scan #{i+1}", size=sizes["medium_text"], weight=ft.FontWeight.BOLD, color=colors["general_info_color"]),
                                                    ft.Text(
                                                        f"Crop Name: {latest_data[i]["data"]["crop_name"]}", 
                                                        size=sizes["small_text"], 
                                                        color=colors["general_info_color"]
                                                    ),
                                                ],
                                            ),
                                            ft.Row(
                                                spacing=10,
                                                controls=[
                                                    ft.Image(src=images["success_rate_icon"]),
                                                    ft.Column(
                                                        spacing=0,
                                                        controls=[
                                                            ft.Text(
                                                                "35%", 
                                                                size=sizes["small_text"], 
                                                                color=colors["prediction_info_data_color"]
                                                            ),
                                                            ft.Text("Success Rate", size=sizes["extra_small_text"], color=colors["prediction_info_name_color"]),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                spacing=15,
                            ),
                            bgcolor=colors["data_container_color"],
                            border_radius=8,
                            padding=ft.padding.all(10),
                            margin=ft.margin.symmetric(vertical=4,horizontal=4),
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=2,
                                color=ft.colors.GREY_400,
                                offset=ft.Offset(0, 2)
                            ),
                        )
                        for i in range(count_data - 1, -1, -1)
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        ),
        expand=True,
        padding=ft.padding.all(20),
    )

    # footer section
    footer = ft.Container(
        bgcolor=colors["body_color"],
        content=ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                            controls=[
                                ft.Image(images["home_selected_icon"]),
                                ft.Text("Home", size=sizes["super_extra_small_text"], color=colors["selected_text_color"]),
                            ]
                        ),
                        on_click=route_to_home,
                        style=ft.ButtonStyle(
                            bgcolor={"": ft.colors.TRANSPARENT},
                            padding=0,
                        ),
                    ),
                    ft.IconButton(
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                            controls=[
                                ft.Image(images["analysis_unselected_icon"]),
                                ft.Text("Analytics", size=sizes["super_extra_small_text"], color=colors["unselected_text_color"]),
                            ]
                        ),
                        on_click=route_to_analytics,
                        style=ft.ButtonStyle(
                            bgcolor={"": ft.colors.TRANSPARENT},
                            padding=0,
                        ),
                    ),
                    ft.IconButton(
                        content=ft.Container(
                            content=ft.Image(images["camera_scan_icon"]),
                            width=50,
                            height=50,
                            border_radius=30,
                            bgcolor=colors["camera_scan_background_color"],
                            alignment=ft.alignment.center,
                        ),
                        on_click=route_to_camera,
                        style=ft.ButtonStyle(
                            bgcolor={"": ft.colors.TRANSPARENT},
                            padding=0,
                        ),
                    ),
                    ft.IconButton(
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                            controls=[
                                ft.Image(images["logs_unselected_icon"]),
                                ft.Text("Logs", size=sizes["super_extra_small_text"], color=colors["unselected_text_color"]),
                            ]
                        ),
                        on_click=route_to_logs,
                        style=ft.ButtonStyle(
                            bgcolor={"": ft.colors.TRANSPARENT},
                            padding=0,
                        ),
                    ),
                    ft.IconButton(
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                            controls=[
                                ft.Image(images["profile_unselected_icon"]),
                                ft.Text("Profile", size=sizes["super_extra_small_text"], color=colors["unselected_text_color"]),
                            ]
                        ),
                        on_click=route_to_profile,
                        style=ft.ButtonStyle(
                            bgcolor={"": ft.colors.TRANSPARENT},
                            padding=0,
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            padding=ft.padding.symmetric(vertical=10),
            bgcolor=colors["navigation_color"],
            border_radius=ft.border_radius.only(top_left=25,top_right=25),
        ),
        height=60
    )

    # combine sections into a single layout
    page.add(
        ft.Column(
            controls=[
                header,
                body,
                footer,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
        )
    )
