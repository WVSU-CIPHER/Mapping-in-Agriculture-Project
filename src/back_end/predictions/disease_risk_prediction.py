# returns detected diseases and its severity levels based on processed images

import openai, json, re
from back_end.config.settings import OPEN_APIS

class CropDiseaseRisk:
    def __init__(self):
        # initializes OpenAI client
        self.client = openai.OpenAI(
            base_url = OPEN_APIS[1]["api_url"],
            api_key = OPEN_APIS[1]["api_key"]
        )
        self.model = OPEN_APIS[1]["model"]
        self.temperature = OPEN_APIS[1]["temperature"]
        self.max_completion_tokens = OPEN_APIS[1]["max_completion_tokens"]
    
    def generate_prompt(self, crop_name: str, disease_name: str, symptoms: str, severity: str, spreading: str) -> str:
        # creates a detailed prompt for the Groq API based on the given inputs.
        # arg. crop_name: name of the crop
        # arg. disease_name: name of the disease
        # arg. symptoms: listed symptoms of the disease in bullet form
        # arg. severity: severity of the disease
        # arg. spreading: spreading of the disease
        # return: a string prompt

        prompt = (
            f"Evaluate the disease risk level for the following crop:\n\n"
            f"Crop Name: {crop_name}\n"
            f"Disease Name (Scientific): {disease_name}\n"
            f"Symptoms: {symptoms}\n"
            f"Severity: {severity}\n"
            f"Spreading: {spreading}\n\n"
            f"Provide a normalized risk level from 0 (high risk) to 1 (healthy). "
            f"Respond with a JSON object containing the risk_value and reasoning, "
            f"e.g., {{'risk_value': 0.7, 'reasoning': 'Explanation here'}}."
        )
        return prompt
    
    def get_risk_value(self, crop_name: str, disease_name: str, symptoms: str, severity: str, spreading: str) -> str:
        # fetches disease risk value from the Groq API
        # arg. crop_name: name of the crop
        # arg. disease_name: name of the disease
        # arg. symptoms: listed symptoms of the disease in bullet form
        # arg. severity: severity of the disease
        # arg. spreading: spreading of the disease
        # return: risk value in float

        # generates the prompt
        prompt = self.generate_prompt(crop_name, disease_name, symptoms, severity, spreading)

        # calls the open api
        response = self.client.chat.completions.create(
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            model = self.model,
            temperature = self.temperature,
            max_completion_tokens = self.max_completion_tokens,
            top_p = 1,
            stop = None,
            stream = False,
        )

        # extracts and returns the risk value
        response = response.choices[0].message.content.strip()
        try:
            json_response = re.sub(r"'", r'"', response)
            parsed_response = json.loads(json_response)
            risk_value = parsed_response.get("risk_value", None)
            reasoning = parsed_response.get("reasoning", "")
            return risk_value, reasoning
        except json.JSONDecodeError:
            raise ValueError(f"Failed to parse AI response: {response}")
    
    def get_risk_indicator_level(self, risk_value: float) -> str:
        # converts a risk value to a risk level indicator through ranges
        # arg. risk_value: risk value from the disease
        # return: risk indicator level

        risk_levels = {
            "High": {"min": 0.0, "max": 0.25},
            "Medium": {"min": 0.25, "max": 0.5},
            "Low": {"min": 0.5, "max": 0.95},
            "Healthy": {"min": 0.95, "max": 1.0},
        }

        for level, range_ in risk_levels.items():
            if range_["min"] <= risk_value < range_["max"]:
                return level
        raise ValueError("Risk value must be between 0 and 1.")

# # [testing purposes]
# if __name__ == "__main__":
#     crop_disease_risk = CropDiseaseRisk()

#     # Sample input
#     crop_details = {
#         "crop_name": "Wheat",
#         "disease_name": "Puccinia graminis (Stem Rust)",
#         "symptoms": "Reddish-brown pustules on stems and leaves, reduced growth",
#         "severity": "Severe",
#         "spreading": "Airborne spores, spread rapidly in warm and moist conditions"
#     }

#     try:
#         # Get disease risk prediction
#         risk_value, reasoning = crop_disease_risk.get_risk_value(**crop_details)
#         print(f"Risk Value: {risk_value}")
#         print(f"Reasoning: {reasoning}")

#         # Get risk level
#         risk_level = crop_disease_risk.get_risk_indicator_level(risk_value)
#         print(f"Risk Level: {risk_level}")
#     except ValueError as e:
#         print(f"Error: {e}")