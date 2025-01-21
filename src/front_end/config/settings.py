# contains configuration settings to be used for front-end side
# (e.g., values for text, image paths, sizes)

MAIN_CONFIG = {
    "title": "AniLyze",
    "scroll": "auto",
    "default_width": 360,
    "default_height": 640,
}

LANDING_PAGE_CONFIG = {
    "scroll": "disable",
    "images": {
        "background_image": "src/assets/landing_background_image.png",
        "top_image": "src/assets/landing_top_blur.png",
        "logo_image": "src/assets/anilyze_logo.png",
    },
    "texts": {
        "title_lines": ["THE FUTURE OF", "AGRICULTURAL MAPPING"],
        "subtitle": "Grow smarter by mapping, monitoring, and maximizing your crop’s potential.",
        "button_text": "Get Started",
    },
    "sizes": {
        "logo_size": 60,
        "title_font_size": 24,
        "subtitle_font_size": 12,
        "button_font_size": 18,
        "button_radius": 25,
        "button_width": 240,
        "button_height": 48,
        "button_border_width": 2,
        "button_bottom_spacing": 20,
    },
    "colors": {
        "title_color": ["#A26821", "#68911B"],
        "subtitle_color": "#000000",
        "button_background_color": "#68911B",
        "button_text_color": "#FFFFFF",
        "button_stroke_color": "#BCC496",
    },
}

HOME_PAGE_CONFIG = {
    "display_count_data": 10,
    "scroll": "disable",
    "images": {
        "location_icon": "src/assets/location_icon.png",
        "weather_icon": "src/assets/cloudy.png",
        "heat_index_icon": "src/assets/heat_index_icon.png",
        "humidity_icon": "src/assets/humidity_icon.png",
        "precipitation_icon": "src/assets/precipitation_icon.png",
        "wind_speed_icon": "src/assets/wind_speed_icon.png",
        "success_rate_icon": "src/assets/success_rate_icon.png",
        "home_selected_icon": "src/assets/home_selected_icon.png",
        "analysis_unselected_icon": "src/assets/analysis_unselected_icon.png",
        "logs_unselected_icon": "src/assets/logs_unselected_icon.png",
        "profile_unselected_icon": "src/assets/profile_unselected_icon.png",
        "camera_scan_icon": "src/assets/camera_scan_icon.png"
    },
    "sizes": {
        "large_text": 18,
        "medium_text": 14,
        "small_text": 12,
        "extra_small_text": 10,
        "super_extra_small_text": 8,
        "button_border_width": 4,
    },
    "colors": {
        "header_color": "#68911B",
        "header_text_color": "#FFFFFF",
        "weather_container_color": "#FFFFFF",
        "weather_info_data_color": "#000000",
        "weather_info_name_color": "#A26821",
        "body_color": "#F6EDED",
        "body_title_color": "#000000",
        "data_container_color": "#FFFFFF",
        "general_info_color": "#000000",
        "prediction_info_data_color": "#1E1E1E",
        "prediction_info_name_color": "#00663A",
        "navigation_color": "#FFFFFF",
        "selected_text_color": "#68911B",
        "unselected_text_color": "#ABAAAA",
        "camera_scan_background_color": "#68911B",
    }
}

ANALYSIS_PAGE_CONFIG = {
    "display_count_data": 1,
    "scroll": "disable",
    "images": {
        "location_icon": "src/assets/location_icon.png",
        "weather_icon": "src/assets/cloudy.png",
        "heat_index_icon": "src/assets/heat_index_icon.png",
        "humidity_icon": "src/assets/humidity_icon.png",
        "precipitation_icon": "src/assets/precipitation_icon.png",
        "wind_speed_icon": "src/assets/wind_speed_icon.png",
        "success_rate_icon": "src/assets/success_rate_icon.png",
        "disease_risk_icon": "src/assets/disease_risk_icon.png",
        "weather_impact_icon": "src/assets/weather_impact_icon.png",
        "home_unselected_icon": "src/assets/home_unselected_icon.png",
        "analysis_selected_icon": "src/assets/analysis_selected_icon.png",
        "logs_unselected_icon": "src/assets/logs_unselected_icon.png",
        "profile_unselected_icon": "src/assets/profile_unselected_icon.png",
        "camera_scan_icon": "src/assets/camera_scan_icon.png"
    },
    "sizes": {
        "large_text": 16,
        "medium_text": 14,
        "small_text": 12,
        "extra_small_text": 10,
        "super_extra_small_text": 8,
        "button_border_width": 4,
    },
    "colors": {
        "header_color": "#68911B",
        "header_text_color": "#FFFFFF",
        "weather_container_color": "#FFFFFF",
        "weather_info_data_color": "#000000",
        "weather_info_name_color": "#A26821",
        "body_color": "#F6EDED",
        "body_title_color": "#000000",
        "data_container_color": "#FFFFFF",
        "general_info_color": "#000000",
        "prediction_info_data_color": "#1E1E1E",
        "prediction_info_name_color": "#00663A",
        "graph_bar_color": "#64780D",
        "graph_grid_color": "#ABAAAA",
        "navigation_color": "#FFFFFF",
        "selected_text_color": "#68911B",
        "unselected_text_color": "#ABAAAA",
        "camera_scan_background_color": "#68911B",
    }
}