# returns series of suggestions based on predictions

import openai
from typing import List
from config.settings import OPEN_APIS

class CropSuggestion:
    def __init__(self):
        # initializes open api as client 
        self.client = openai.OpenAI(
            base_url = OPEN_APIS[0]["api_url"],
            api_key = OPEN_APIS[0]["api_key"]
        )
        self.temperature = OPEN_APIS[0]["temperature"]
        self.max_completion_tokens = OPEN_APIS[0]["max_completion_tokens"]

    def generate_prompt(self, crop_name: str, disease_name: str, success_rate: float, harvest_date: str, weather_risks: List[str], disease_risks: List[str], treatments: List[str]) -> str:
        # creates a detailed prompt for the Groq API based on the given inputs.
        # arg. crop_name: name of the crop
        # arg. disease_name: name of the disease in string
        # arg. success_rate: estimated success rate of the crop
        # arg. harvest_date: expected harvest date
        # arg. weather_risks: dictionary containing weather risk levels (temperature_risk, precipitation_risk, wind_risk)
        # arg. disease_risks: dictionary containing disease risk details (symptoms, severity, spread)
        # arg. treatments: dictionary containing treatment methods (prevention, chemical_treatment, biological_treatment)
        # return: a string prompt
        
        prompt = (
            f"Provide actionable suggestions for a farmer based on the following information:\n"
            f"- Crop Name: {crop_name}\n"
            f"- Disease Name (Scientific): {disease_name}\n"
            f"- Estimated Success Rate: {success_rate}%\n"
            f"- Expected Harvest Date: {harvest_date}\n"
            f"- Weather Risk Levels:\n"
            f"  - Temperature Risk: {weather_risks.get('temperature_risk', 'Unknown')}\n"
            f"  - Precipitation Risk: {weather_risks.get('precipitation_risk', 'Unknown')}\n"
            f"  - Wind Speed Risk: {weather_risks.get('wind_speed_risk', 'Unknown')}\n"
            f"- Disease Risk Details:\n"
            f"  - Symptoms: {disease_risks.get('symptoms', 'Unknown')}\n"
            f"  - Severity: {disease_risks.get('severity', 'Unknown')}\n"
            f"  - Spread: {disease_risks.get('spread', 'Unknown')}\n"
            f"- Treatment Options:\n"
            f"  - Prevention: {treatments.get('prevention', 'Unknown')}\n"
            f"  - Chemical Treatment: {treatments.get('chemical_treatment', 'Unknown')}\n"
            f"  - Biological Treatment: {treatments.get('biological_treatment', 'Unknown')}\n"
            f"Make all suggestions easy for farmers to understand. Use agricultural terms, but avoid technical jargon. " 
            f"Format the suggestions as a single-level bullet list. Ensure there are no extra spaces or inconsistencies before and after the bullet points."
        )
        return prompt

    def get_suggestions(self, crop_name: str, disease_name: str, success_rate: float, harvest_date: str, weather_risks: List[str], disease_risks: List[str], treatments: List[str]):
        # fetches actionable suggestions for a farmer using the Groq API.
        # arg. crop_name: name of the crop
        # arg. disease_name: name of the disease in string
        # arg. success_rate: estimated success rate of the crop
        # arg. harvest_date: expected harvest date
        # arg. weather_risks: dictionary containing weather risk levels (temperature_risk, precipitation_risk, wind_risk)
        # arg. disease_risks: dictionary containing disease risk details (symptoms, severity, spread)
        # arg. treatments: dictionary containing treatment methods (prevention, chemical_treatment, biological_treatment)
        # return: suggestions as a string
        
        # generates the prompt
        prompt = self.generate_prompt(
            crop_name, disease_name, success_rate, harvest_date, weather_risks, disease_risks, treatments
        )

        # calls the open api
        response = self.client.chat.completions.create(
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            model = "llama-3.3-70b-versatile",
            temperature = self.temperature,
            max_completion_tokens = self.max_completion_tokens,
            top_p = 1,
            stop = None,
            stream = False,
        )

        # extracts and returns the suggestions
        return response.choices[0].message.content.strip()

# # [testing purposes]
# if __name__ == "__main__":
#     suggestor = CropSuggestion()

#     # Example input details
#     crop_details = {
#         "crop_name": "Wheat",
#         "disease_name": "Puccinia graminis",
#         "success_rate": 85,
#         "harvest_date": "2025-03-15",
#         "weather_risks": {
#             "temperature_risk": "High", 
#             "precipitation_risk": "Medium", 
#             "wind_speed_risk": "Low"
#         },
#         "disease_risks": {
#             "symptoms": "Rusty pustules on leaves", 
#             "severity": "High", 
#             "spread": "Airborne"
#         },
#         "treatments": {
#             "prevention": "Use resistant varieties.",
#             "chemical_treatment": "Apply fungicides like Propiconazole.",
#             "biological_treatment": "Introduce Trichoderma harzianum."
#         },
#     }

#     # Get suggestions
#     suggestions = suggestor.get_suggestions(**crop_details)
#     print(f"Suggestions:\n{suggestions}")