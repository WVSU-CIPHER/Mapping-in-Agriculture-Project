import flet as ft

def main(page: ft.Page):
    page.title = "Farmer Dashboard"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ALWAYS

    def responsive_size(screen_width):
        if screen_width <= 360:
            return 12, 16, 18, 50
        elif screen_width <= 768:
            return 14, 18, 20, 75
        else:
            return 18, 22, 32, 150

    # Dynamically set sizes based on screen width
    small_text_size, medium_text_size, large_text_size, image_size = responsive_size(page.window_width)

    # Define Home Page
    def home_page():
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.Container(
                        bgcolor=ft.colors.GREEN_200,
                        padding=20,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.START,
                            spacing=20,
                            controls=[
                                # Header Section
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Column(
                                            alignment=ft.MainAxisAlignment.START,
                                            spacing=5,
                                            controls=[
                                                ft.Text("Hello, Farmer!", size=large_text_size, color=ft.colors.BLACK),
                                                ft.Text("Monday, 20 Jan 2025", size=medium_text_size, color=ft.colors.BLACK),
                                            ],
                                        ),
                                        ft.Column(
                                            alignment=ft.MainAxisAlignment.END,
                                            spacing=5,
                                            controls=[
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.END,
                                                    controls=[
                                                        ft.Icon(ft.icons.LOCATION_ON, color=ft.colors.BLACK),
                                                        ft.Text("Iloilo, Philippines", size=small_text_size, color=ft.colors.BLACK),
                                                    ],
                                                ),
                                                ft.Text("30°C", size=medium_text_size, color=ft.colors.BLACK),
                                            ],
                                        ),
                                    ],
                                ),

                                # Weather Info
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        ft.Column([
                                            ft.Icon(ft.icons.THERMOSTAT, color=ft.colors.ORANGE),
                                            ft.Text("36.2°C", size=medium_text_size),
                                            ft.Text("Heat Index", size=small_text_size),
                                        ]),
                                        ft.Column([
                                            ft.Icon(ft.icons.WATER_DROP, color=ft.colors.BLUE),
                                            ft.Text("2.5%", size=medium_text_size),
                                            ft.Text("Humidity", size=small_text_size),
                                        ]),
                                        ft.Column([
                                            ft.Icon(ft.icons.CLOUD, color=ft.colors.GREY),
                                            ft.Text("0.1 mm", size=medium_text_size),
                                            ft.Text("Rainfall", size=small_text_size),
                                        ]),
                                        ft.Column([
                                            ft.Icon(ft.icons.AIR, color=ft.colors.GREEN),
                                            ft.Text("6.9 m/s", size=medium_text_size),
                                            ft.Text("Wind Speed", size=small_text_size),
                                        ]),
                                    ],
                                ),

                                # Farm List
                                ft.Text("Farm List", size=large_text_size, weight=ft.FontWeight.BOLD),
                                ft.ListView(
                                    spacing=10,
                                    controls=[
                                        ft.Container(
                                            bgcolor=ft.colors.WHITE,
                                            padding=15,
                                            border_radius=10,
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.START,
                                                controls=[
                                                    ft.Image(
                                                        src="https://via.placeholder.com/150",  # Replace with crop image
                                                        width=image_size,
                                                        height=image_size,
                                                        fit=ft.ImageFit.COVER,
                                                    ),
                                                    ft.Column(
                                                        alignment=ft.MainAxisAlignment.START,
                                                        spacing=5,
                                                        controls=[
                                                            ft.Text("Tanom ni Brey", size=medium_text_size, weight=ft.FontWeight.BOLD),
                                                            ft.Text("Crop Type: Corn", size=small_text_size, color=ft.colors.BLACK54),
                                                            ft.Row(
                                                                alignment=ft.MainAxisAlignment.START,
                                                                controls=[
                                                                    ft.Icon(ft.icons.CALENDAR_TODAY, size=small_text_size, color=ft.colors.ORANGE),
                                                                    ft.Text("Estimated: 2d 9h 10m", size=small_text_size, color=ft.colors.BLACK54),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    ft.Text("01 Jan 2025", size=small_text_size, color=ft.colors.BLACK54),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),

                                # Bottom Navigation Bar
                                ft.Container(
                                    bgcolor=ft.colors.WHITE,
                                    padding=10,
                                    border_radius=10,
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                        controls=[
                                            ft.IconButton(
                                                icon=ft.icons.HOME,
                                                icon_size=medium_text_size,
                                                tooltip="Home",
                                                icon_color=ft.colors.GREEN,  # Active page color
                                                on_click=lambda _: page.go("/"),
                                            ),
                                            ft.IconButton(
                                                icon=ft.icons.ANALYTICS,
                                                icon_size=medium_text_size,
                                                tooltip="Analysis",
                                                on_click=lambda _: page.go("/analysis"),
                                            ),
                                            ft.IconButton(
                                                icon=ft.icons.CAMERA,
                                                icon_size=medium_text_size,
                                                tooltip="Scan Crops",
                                            ),
                                            ft.IconButton(
                                                icon=ft.icons.BOOK,
                                                icon_size=medium_text_size,
                                                tooltip="Logs",
                                            ),
                                            ft.IconButton(
                                                icon=ft.icons.PERSON,
                                                icon_size=medium_text_size,
                                                tooltip="Profile",
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            )
        )
        page.update()

    # Define Analysis Page
    def analysis_page():
        page.views.clear()
        page.views.append(
            ft.View(
                route="/analysis",
                scroll="auto",
                controls=[
                    ft.Container(
                        bgcolor=ft.colors.GREEN_200,
                        padding=20,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Column(
                                    alignment=ft.MainAxisAlignment.START,
                                    controls=[
                                        ft.Text("Hello, Farmer!", size=22, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                        ft.Text("Monday, 20 Jan 2025", size=16, color=ft.colors.BLACK),
                                    ],
                                ),
                                ft.Column(
                                    alignment=ft.MainAxisAlignment.END,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.END,
                                            controls=[
                                                ft.Icon(ft.icons.LOCATION_ON, color=ft.colors.BLACK),
                                                ft.Text("Iloilo, Philippines", size=14, color=ft.colors.BLACK),
                                            ],
                                        ),
                                        ft.Text("30°C", size=16, color=ft.colors.BLACK),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    ft.Column(
                        controls=[
                            ft.Container(
                                padding=20,
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Icon(ft.icons.THERMOSTAT, color=ft.colors.ORANGE),
                                                ft.Text("36.2°C", size=14),
                                                ft.Text("Heat Index", size=12),
                                            ],
                                        ),
                                        ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Icon(ft.icons.WATER_DROP, color=ft.colors.BLUE),
                                                ft.Text("2.5%", size=14),
                                                ft.Text("Humidity", size=12),
                                            ],
                                        ),
                                        ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Icon(ft.icons.CLOUD, color=ft.colors.GREY),
                                                ft.Text("0.1 mm", size=14),
                                                ft.Text("Rainfall", size=12),
                                            ],
                                        ),
                                        ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Icon(ft.icons.AIR, color=ft.colors.GREEN),
                                                ft.Text("6.9 m/s", size=14),
                                                ft.Text("Wind Speed", size=12),
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                            ft.Container(
                                padding=20,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.START,
                                    controls=[
                                        ft.Text("Crop Forecast", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                        ft.Container(
                                            bgcolor=ft.colors.WHITE,
                                            padding=15,
                                            border_radius=10,
                                            content=ft.Column(
                                                controls=[
                                                    ft.Row(
                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                        controls=[
                                                            ft.Text("Tanom ni Brey", size=18, weight=ft.FontWeight.BOLD),
                                                            ft.Text("01 Jan 2025", size=14, color=ft.colors.BLACK54),
                                                        ],
                                                    ),
                                                    ft.Text("Crop Type: Corn", size=14, color=ft.colors.BLACK54),
                                                    ft.Text("Crop Status: Healthy", size=14, color=ft.colors.BLACK54),
                                                    ft.Text("Last Analysis: 19 Jan 2025", size=14, color=ft.colors.BLACK54),
                                                    ft.Row(
                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                        controls=[
                                                            ft.Column(
                                                                controls=[
                                                                    ft.Text("80% Crop Progress", size=16, weight=ft.FontWeight.BOLD),
                                                                ],
                                                            ),
                                                            ft.Column(
                                                                controls=[
                                                                    ft.Row(
                                                                        controls=[
                                                                            ft.Icon(ft.icons.TIMER, color=ft.colors.ORANGE),
                                                                            ft.Text("Estimated: 2d 9h 10m", size=14, color=ft.colors.BLACK54),
                                                                        ],
                                                                    ),
                                                                    ft.Row(
                                                                        controls=[
                                                                            ft.Text("Disease Risk: 1d 8h 5m", size=14, color=ft.colors.BLACK54),
                                                                        ],
                                                                    ),
                                                                    ft.Row(
                                                                        controls=[
                                                                            ft.Icon(ft.icons.INSERT_CHART, color=ft.colors.BLUE),
                                                                            ft.Text("Confidence: 9/10", size=14, color=ft.colors.BLACK54),
                                                                        ],
                                                                    ),
                                                                    ft.Row(
                                                                        controls=[
                                                                            ft.Icon(ft.icons.WIND_POWER, color=ft.colors.YELLOW),
                                                                            ft.Text("Extreme Weather: 5d 3h", size=14, color=ft.colors.BLACK54),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            ft.Container(
                                padding=20,
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    controls=[
                                        ft.Container(
                                            bgcolor=ft.colors.WHITE,
                                            padding=15,
                                            border_radius=10,
                                            expand=True,
                                            content=ft.Column(
                                                controls=[
                                                    ft.Text("Disease Risk Level", size=16, weight=ft.FontWeight.BOLD),
                                                ],
                                            ),
                                        ),
                                        ft.Container(
                                            bgcolor=ft.colors.WHITE,
                                            padding=15,
                                            border_radius=10,
                                            expand=True,
                                            content=ft.Column(
                                                controls=[
                                                    ft.Text("Harvest Success Rate", size=16, weight=ft.FontWeight.BOLD),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    ft.Container(
                        bgcolor=ft.colors.WHITE,
                        padding=10,
                        border_radius=10,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.IconButton(icon=ft.icons.HOME, tooltip="Home", on_click=lambda _: page.go("/")),
                                ft.IconButton(icon=ft.icons.ANALYTICS, icon_color=ft.colors.GREEN, tooltip="Analysis", on_click=lambda _: page.go("/analysis")),
                                ft.IconButton(icon=ft.icons.CAMERA, tooltip="Scan Crops"),
                                ft.IconButton(icon=ft.icons.BOOK, tooltip="Logs"),
                                ft.IconButton(icon=ft.icons.PERSON, tooltip="Profile"),
                            ],
                        ),
                    ),
                ],
            )
        )
        page.update()


    # Handle routing
    page.on_route_change = lambda e: home_page() if page.route == "/" else analysis_page()

        # Start with home page
    home_page()

ft.app(target=main)
