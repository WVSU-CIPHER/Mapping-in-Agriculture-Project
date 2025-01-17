# returns a certain value, dictionary, or info from json

from typing import Dict, List

class CropInfo:
    def get_top_prediction(results: List[Dict]) -> Dict:
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
    
    def get_top_crop_name(result: Dict, in_scientific: bool = False) -> str:
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

    def get_all_crop_names(result: Dict, in_scientific: bool = False) -> List[str]:
        # returns all predicted crop names from the result
        # arg. result: crop prediction in json format
        # return: list of crop names in string
        crop_names = []

        crop_suggestions = result.get("result", {}).get("crop", {}).get("suggestions", [])
        for suggestion in crop_suggestions:
            crop_names.append(suggestion["name"] if not in_scientific else suggestion["scientific_name"])

        return crop_names
    
    def get_top_disease_name(result: Dict, in_scientific: bool = False) -> str:
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
    
    def get_all_disease_names(result: Dict, in_scientific: bool = False) -> List[str]:
        # returns all predicted disease names from the result
        # arg. result: crop prediction in json format
        # return: list of disease names in string
        disease_names = []

        disease_suggestions = result.get("result", {}).get("disease", {}).get("suggestions", [])
        for suggestion in disease_suggestions:
            disease_names.append(suggestion["name"] if not in_scientific else suggestion["scientific_name"])

        return disease_names