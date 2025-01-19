# contains configuration settings to be used globally
# (e.g., api keys, database urls if necessary)

CROP_DETECTION_APIS = [
    {
        "api_url": "https://crop.kindwise.com/api/v1/identification?details=common_names,type,taxonomy,eppo_code,eppo_regulation_status,gbif_id,image,images,wiki_url,wiki_description,treatment,description,symptoms,severity,spreading&language=en",
        "api_key": "LjGRHyw1lUBvE3h5meya26m81hBZ5qVP5CHN6iE9bqzgoG6F4L"
    }
]

WEATHER_APIS = [
    {
        "api_url": "https://api.open-meteo.com/v1/forecast",
        "params": {
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max",
            "timezone": "Asia/Manila"
        }
    },
    {
        "api_url": "https://api.open-meteo.com/v1/forecast",
        "params": {
            'hourly': 'temperature_2m,relative_humidity_2m,rain,wind_speed_10m',
            'current_weather': True,
        }
    }
]

OPEN_APIS = [
    {   # suggestion_guess.py
        "api_url": "https://api.groq.com/openai/v1",
        "api_key": "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",
        "temperature": 0.5,
        "max_completion_tokens": 512
    },
    {   # disease_risk_prediction.py
        "api_url": "https://api.groq.com/openai/v1",
        "api_key": "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",
        "temperature": 0.5,
        "max_completion_tokens": 256
    }
]

SUCCESS_RATE_WEIGHTED_AVERAGE = {
    "geolocation_score_weight": 0.18,
    "temperature_score_weight": 0.24,
    "precipitation_score_weight": 0.22,
    "wind_speed_score_weight": 0.08,
    "disease_score_weight": 0.28
}