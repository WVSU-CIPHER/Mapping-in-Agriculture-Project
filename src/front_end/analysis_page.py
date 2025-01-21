# analysis page for the app

import flet as ft
from front_end.config.settings import ANALYSIS_PAGE_CONFIG
from back_end.geolocation import GeoLocation, DateTime
from back_end.weather_info import WeatherInfo
from back_end.database import Database

def analysis_page(page: ft.Page, navigate_to):
    
    page.scroll = ANALYSIS_PAGE_CONFIG["scroll"]
    config = ANALYSIS_PAGE_CONFIG
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
        from front_end.home_page import home_page
        navigate_to(lambda p: home_page(p, navigate_to))
        
    def route_to_analytics(e):
        pass
        
    def route_to_camera(e):
        from front_end.scan_page import scan_page
        navigate_to(lambda p: scan_page(p, navigate_to))
        
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
                                            f"{round(weather_info.get_temperature(), 2)}°C", 
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
                                        f"{round(weather_info.get_heat_index(), 2)}°C", 
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
                                        f"{round(weather_info.get_humidity(), 2)}%", 
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
                                        f"{round(weather_info.get_rainfall(), 2)} mm", 
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
                                        f"{round(weather_info.get_wind_speed(), 2)} m/s", 
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
        content=ft.ListView(
            controls=[
                ft.Container(
                    margin=ft.margin.only(left=20,bottom=10),
                    content=ft.Text(
                        "Crop Forecast",
                        size=sizes["medium_text"],
                        weight=ft.FontWeight.BOLD,
                        color=colors["body_title_color"]
                    ),
                ),

                # general information of latest crop
                ft.Container(
                    margin=ft.margin.symmetric(horizontal=20),
                    padding=ft.padding.all(20),
                    bgcolor=colors["data_container_color"],
                    border_radius=8,
                    content=ft.Column([
                        ft.Text("Latest Farm", size=sizes["medium_text"], weight=ft.FontWeight.BOLD, color=colors["general_info_color"]),
                        ft.Container(
                            height=200,
                            border_radius=8,
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            content=ft.Image(
                                src=latest_data[0]["data"]["image_url"],
                                fit=ft.ImageFit.COVER,
                            ),
                        ),
                        ft.Container(
                            content=ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Row([
                                        ft.Text(
                                            "Crop Name: ",
                                            size=sizes["small_text"],
                                            color=colors["prediction_info_data_color"]
                                        ),
                                        ft.Text(
                                            latest_data[0]['data']['crop_name'],
                                            size=sizes["small_text"],
                                            weight=ft.FontWeight.BOLD,
                                            color=colors["prediction_info_data_color"]
                                        ),
                                    ]),
                                    ft.Row([
                                        ft.Text(
                                            "Disease Name: ",
                                            size=sizes["small_text"],
                                            color=colors["prediction_info_data_color"]
                                        ),
                                        ft.Text(
                                            latest_data[0]['data']['disease_risks']['disease_name'],
                                            size=sizes["small_text"],
                                            weight=ft.FontWeight.BOLD,
                                            color=colors["prediction_info_data_color"]
                                        ),
                                    ]),
                                    ft.Row([
                                        ft.Text(
                                            "Last Analysis: ",
                                            size=sizes["small_text"],
                                            color=colors["prediction_info_data_color"]
                                        ),
                                        ft.Text(
                                            latest_data[0]['datetime']['date'],
                                            size=sizes["small_text"],
                                            weight=ft.FontWeight.BOLD,
                                            color=colors["prediction_info_data_color"]
                                        ),
                                    ]),
                                ]
                            ),
                        ),
                        ft.Container(height=5),
                        ft.Container(
                            content=ft.Column(
                                spacing=2,
                                controls=[
                                    ft.Row([
                                        ft.Image(src=images["success_rate_icon"]),
                                        ft.Column(
                                            spacing=0,
                                            controls=[
                                            ft.Text(
                                                f"{round((latest_data[0]['data']['prediction']['success_rate'] * 100.0), 2)}%", 
                                                size=sizes["small_text"],
                                                weight=ft.FontWeight.BOLD,
                                                color=colors["prediction_info_data_color"]
                                            ),
                                            ft.Text(
                                                "Success Rate", 
                                                size=sizes["extra_small_text"],
                                                color=colors["prediction_info_name_color"]
                                            ),
                                        ]),
                                    ]),
                                    ft.Row([
                                        ft.Image(src=images["disease_risk_icon"]),
                                        ft.Column(
                                            spacing=0,
                                            controls=[
                                            ft.Text(
                                                f"{latest_data[0]['data']['prediction']['disease_impact']['risk_level']}", 
                                                size=sizes["small_text"],
                                                weight=ft.FontWeight.BOLD,
                                                color=colors["prediction_info_data_color"]
                                            ),
                                            ft.Text(
                                                "Disease Risk Level", 
                                                size=sizes["extra_small_text"],
                                                color=colors["prediction_info_name_color"]
                                            ),
                                        ]),
                                    ]),
                                    ft.Row([
                                        ft.Image(src=images["weather_impact_icon"]),
                                        ft.Column(
                                            spacing=0,
                                            controls=[
                                            ft.Text(
                                                f"{latest_data[0]['data']['prediction']['weather_impact']['overall_risk_level']}", 
                                                size=sizes["small_text"],
                                                weight=ft.FontWeight.BOLD,
                                                color=colors["prediction_info_data_color"]
                                            ),
                                            ft.Text(
                                                "Weather Impact Level", 
                                                size=sizes["extra_small_text"],
                                                color=colors["prediction_info_name_color"]
                                            ),
                                        ]),
                                    ]),
                                ]
                            ),
                        ),
                    ]),
                ),

                # weather impact risk levels of the crop
                ft.Container(
                    margin=ft.margin.symmetric(horizontal=20, vertical=10),
                    padding=ft.padding.all(20),
                    bgcolor=colors["data_container_color"],
                    border_radius=8,
                    content=ft.Column([
                        ft.Text(
                            "Weather Impact Risk Levels",
                            size=sizes["medium_text"],
                            weight=ft.FontWeight.BOLD,
                            color=colors["general_info_color"],
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Container(
                            padding=10,
                            height=300,
                            content=ft.BarChart(
                                bar_groups=[
                                    ft.BarChartGroup(
                                        x=0,
                                        bar_rods=[
                                            ft.BarChartRod(
                                                from_y=0,
                                                to_y=float(latest_data[0]["data"]["prediction"]["weather_impact"]["temperature"]),
                                                color=ft.colors.BLUE,
                                                width=40,
                                                tooltip="Temperature",
                                                border_radius=2,
                                            ),
                                        ],
                                    ),
                                    ft.BarChartGroup(
                                        x=1,
                                        bar_rods=[
                                            ft.BarChartRod(
                                                from_y=0,
                                                to_y=float(latest_data[0]["data"]["prediction"]["weather_impact"]["precipitation"]),
                                                color=ft.colors.GREEN,
                                                width=40,
                                                tooltip="Precipitation",
                                                border_radius=2,
                                            ),
                                        ],
                                    ),
                                    ft.BarChartGroup(
                                        x=2,
                                        bar_rods=[
                                            ft.BarChartRod(
                                                from_y=0,
                                                to_y=float(latest_data[0]["data"]["prediction"]["weather_impact"]["wind_speed"]),
                                                color=ft.colors.ORANGE,
                                                width=40,
                                                tooltip="Wind Speed",
                                                border_radius=2,
                                            ),
                                        ],
                                    ),
                                ],
                                border=ft.border.all(1, ft.colors.GREY_400),
                                left_axis=ft.ChartAxis(
                                    labels=[ft.Text(str(i)) for i in range(0, 101, 20)],
                                    labels_size=12,
                                ),
                                bottom_axis=ft.ChartAxis(
                                    labels=[
                                        ft.Text("Temperature"),
                                        ft.Text("Precipitation"),
                                        ft.Text("Wind Speed"),
                                    ],
                                    labels_size=12,
                                ),
                                horizontal_grid_lines=ft.ChartGridLines(
                                    color=ft.colors.GREY_300,
                                    interval=20,
                                    width=1,
                                ),
                                max_y=100,
                                interactive=True,
                                expand=True,
                            ),
                            border=ft.border.all(1, ft.colors.GREY_400),
                            border_radius=8,
                        ),
                    ]),
                ),

                # suggestions for the crop
                ft.Container(
                    margin=ft.margin.symmetric(horizontal=20),
                    padding=ft.padding.all(20),
                    bgcolor=colors["data_container_color"],
                    border_radius=8,
                    content=ft.Column([
                        ft.Text(
                            "Suggestions",
                            size=sizes["medium_text"],
                            weight=ft.FontWeight.BOLD,
                            color=colors["general_info_color"],
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Text(
                            f"{latest_data[0]["data"]["prediction"]["suggestions"]}",
                            size=sizes["extra_small_text"],
                            color=colors["prediction_info_data_color"]
                        ),
                    ]),
                ),
                ft.Container(height=10),
            ]
        ),
        bgcolor=colors["body_color"],
        expand=True,
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
                                ft.Image(images["home_unselected_icon"]),
                                ft.Text("Home", size=sizes["super_extra_small_text"], color=colors["unselected_text_color"]),
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
                                ft.Image(images["analysis_selected_icon"]),
                                ft.Text("Analytics", size=sizes["super_extra_small_text"], color=colors["selected_text_color"]),
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
