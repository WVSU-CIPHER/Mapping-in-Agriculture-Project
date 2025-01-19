# returns a certain value, dictionary, or info from json

from typing import Dict, List

class CropInfo:
    def get_top_prediction(self, results: List[Dict]) -> Dict:
        # returns the top prediction with the highest probability from suggested crops
        # arg. result: list of crop predictions in json format
        # return: the complete json for the prediction with the highest probability
        max_probability = 0
        highest_probability_result = None

        # evaluates all predictions
        for prediction in results:
            try:
                crop_suggestions = prediction.get("result", {}).get("crop", {}).get("suggestions", [])
                for suggestion in crop_suggestions:
                    if suggestion.get("probability", 0) > max_probability:
                        max_probability = suggestion["probability"]
                        highest_probability_result = prediction
            except KeyError as e:
                print("KeyError while processing prediction:", e)

        return highest_probability_result
    
    def get_top_crop_name(self, result: Dict, in_scientific: bool = False) -> str:
        # returns the crop name with the highest probability from suggested crops
        # arg. result: crop prediction in json format
        # return: crop name in string
        max_probability = 0
        crop_name = None

        crop_suggestions = result.get("result", {}).get("crop", {}).get("suggestions", [])
        for suggestion in crop_suggestions:
            if suggestion.get("probability", 0) > max_probability:
                max_probability = suggestion["probability"]
                crop_name = suggestion["name"] if not in_scientific else suggestion["scientific_name"]
        
        return crop_name

    def get_all_crop_names(self, result: Dict, in_scientific: bool = False) -> List[str]:
        # returns all predicted crop names from the result
        # arg. result: crop prediction in json format
        # return: list of crop names in string
        crop_names = []

        crop_suggestions = result.get("result", {}).get("crop", {}).get("suggestions", [])
        for suggestion in crop_suggestions:
            crop_names.append(suggestion["name"] if not in_scientific else suggestion["scientific_name"])

        return crop_names
    
    def get_top_disease_name(self, result: Dict, in_scientific: bool = False) -> str:
        # returns the disease name with the highest probability from suggested crops
        # arg. result: crop prediction in json format
        # return: disease name in string
        max_probability = 0
        disease_name = None

        disease_suggestions = result.get("result", {}).get("disease", {}).get("suggestions", [])
        for suggestion in disease_suggestions:
            if suggestion.get("probability", 0) > max_probability:
                max_probability = suggestion["probability"]
                disease_name = suggestion["name"] if not in_scientific else suggestion["scientific_name"]

        return disease_name
    
    def get_all_disease_names(self, result: Dict, in_scientific: bool = False) -> List[str]:
        # returns all predicted disease names from the result
        # arg. result: crop prediction in json format
        # return: list of disease names in string
        disease_names = []

        disease_suggestions = result.get("result", {}).get("disease", {}).get("suggestions", [])
        for suggestion in disease_suggestions:
            disease_names.append(suggestion["name"] if not in_scientific else suggestion["scientific_name"])

        return disease_names
    
    def _get_top_disease(self, result: Dict):
        # returns the disease with the highest probability from the result in json form
        # arg. result: crop prediction in json format
        # return: disease in json form
        diseases = result.get("result", {}).get("disease", {}).get("suggestions", [])
        return max(diseases, key=lambda disease: disease["probability"])
    
    def get_all_disease_symptoms(self, result: Dict) -> str:
        # returns all symptoms of the disease from the result
        # arg. result: crop prediction in json format
        # return: symptoms in bullet form with format: name - description
        disease = self._get_top_disease(result)
        symptoms = disease["details"].get("symptoms", {})
        return "\n".join(f"- {name}:{description}" for name, description in symptoms.items())
    
    def get_disease_severity(self, result: Dict) -> str:
        # returns the severity of the disease from the result
        # arg. result: crop prediction in json format
        # return: severity in string
        disease = self._get_top_disease(result)
        return disease["details"].get("severity", "Severity not available.")
    
    def get_disease_spreading(self, result: Dict) -> str:
        # returns the spreading of the disease from the result
        # arg. result: crop prediction in json format
        # return: spreading in string
        disease = self._get_top_disease(result)
        return disease["details"].get("spreading", "Spreading information not available.")
    
    def get_all_prevention_treatment(self, result: Dict) -> str:
        # returns all preventions for the disease from the result
        # arg. result: crop prediction in json format
        # return: preventions in bullet form
        disease = self._get_top_disease(result)
        prevention = disease["details"]["treatment"].get("prevention", [])
        return "\n".join(f"- {item}" for item in prevention)
    
    def get_all_chemical_treatment(self, result: Dict) -> str:
        # returns all chemical treatments for the disease from the result
        # arg. result: crop prediction in json format
        # return: chemical treatments in bullet form
        disease = self._get_top_disease(result)
        chemical_treatment = disease["details"]["treatment"].get("chemical treatment", [])
        return "\n".join(f"- {item}" for item in chemical_treatment)
    
    def get_all_biological_treatment(self, result: Dict) -> str:
        # returns all biological treatments for the disease from the result
        # arg. result: crop prediction in json format
        # return: biological treatments in bullet form
        disease = self._get_top_disease(result)
        biological_treatment = disease["details"]["treatment"].get("biological treatment", [])
        return "\n".join(f"- {item}" for item in biological_treatment)
    
    def get_image_url(self, result: Dict):
        # returns an image used from the result
        # arg. result: crop prediction in json format
        # return: image in jpg
        image_url = result["input"]["images"][0]
        return image_url