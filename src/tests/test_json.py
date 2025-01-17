from back_end.crop_info import CropInfo

RESPONSE = {
  "access_token": "rhprtaSkMQP1Zll",
  "model_version": "crop_health:1.1.1",
  "custom_id": None,
  "input": {
    "latitude": 49.207,
    "longitude": 16.608,
    "similar_images": True,
    "images": [
      "https://crop.kindwise.com/media/images/c10151ec4c2446e89cb40309667265ce.jpg"
    ],
    "datetime": "2024-03-08T10:27:12.887534+00:00"
  },
  "result": {
    "is_plant": {
      "probability": 1,
      "threshold": 0.5,
      "binary": True
    },
    "disease": {
      "suggestions": [
        {
          "id": "b9ec757fefb92520",
          "name": "late blight",
          "probability": 0.9806,
          "similar_images": [
            {
              "id": "100ac65780f4761e7bfd42b8db30fd1ec36fc5e8",
              "url": "https://crop-health.ams3.cdn.digitaloceanspaces.com/similar_images/1/100/ac65780f4761e7bfd42b8db30fd1ec36fc5e8.jpg",
              "license_name": "CC BY 3.0",
              "license_url": "https://creativecommons.org/licenses/by/3.0/",
              "citation": "Howard F. Schwartz, Colorado State University",
              "similarity": 0.789,
              "url_small": "https://crop-health.ams3.cdn.digitaloceanspaces.com/similar_images/1/100/ac65780f4761e7bfd42b8db30fd1ec36fc5e8.small.jpg"
            },
            {
              "id": "111fe91bae90b085eff701f6d57cfba7cebc8412",
              "url": "https://crop-health.ams3.cdn.digitaloceanspaces.com/similar_images/1/111/fe91bae90b085eff701f6d57cfba7cebc8412.jpg",
              "license_name": "CC BY 3.0",
              "license_url": "https://creativecommons.org/licenses/by/3.0/",
              "citation": "Howard F. Schwartz, Colorado State University",
              "similarity": 0.756,
              "url_small": "https://crop-health.ams3.cdn.digitaloceanspaces.com/similar_images/1/111/fe91bae90b085eff701f6d57cfba7cebc8412.small.jpg"
            }
          ],
          "details": {
            "language": "en",
            "entity_id": "b9ec757fefb92520"
          },
          "scientific_name": "Phytophthora infestans"
        },
        {
          "id": "c35556c0c67c0591",
          "name": "healthy",
          "probability": 0.0103,
          "similar_images": [
            {
              "id": "d3a36ce3f543b20f735540db833f8431dc9b35a1",
              "url": "https://crop-health.ams3.cdn.digitaloceanspaces.com/similar_images/1/d3a/36ce3f543b20f735540db833f8431dc9b35a1.jpeg",
              "license_name": "CC0",
              "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
              "citation": "Mars",
              "similarity": 0.596,
              "url_small": "https://crop-health.ams3.cdn.digitaloceanspaces.com/similar_images/1/d3a/36ce3f543b20f735540db833f8431dc9b35a1.small.jpeg"
            },
            {
              "id": "760108c67e39894c5fa9d7ed64b8caf06283218b",
              "url": "https://crop-health.ams3.cdn.digitaloceanspaces.com/similar_images/1/760/108c67e39894c5fa9d7ed64b8caf06283218b.jpeg",
              "license_name": "CC0",
              "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
              "citation": "Amy Kramer",
              "similarity": 0.562,
              "url_small": "https://crop-health.ams3.cdn.digitaloceanspaces.com/similar_images/1/760/108c67e39894c5fa9d7ed64b8caf06283218b.small.jpeg"
            }
          ],
          "details": {
            "language": "en",
            "entity_id": "c35556c0c67c0591"
          },
          "scientific_name": "healthy"
        }
      ]
    },
    "crop": {
      "suggestions": [
        {
          "id": "2746768c8d99bfbb",
          "name": "potato",
          "probability": 0.8785,
          "similar_images": [
            {
              "id": "9b273d5f693bb69b892c0c3b6a30ac2e6758815d",
              "url": "https://crop-health.ams3.cdn.digitaloceanspaces.com/similar_images/1/9b2/73d5f693bb69b892c0c3b6a30ac2e6758815d.jpeg",
              "similarity": 0.693,
              "url_small": "https://crop-health.ams3.cdn.digitaloceanspaces.com/similar_images/1/9b2/73d5f693bb69b892c0c3b6a30ac2e6758815d.small.jpeg"
            },
            {
              "id": "adc7436c0d6739c6e1bc15efd6881455c156f98c",
              "url": "https://crop-health.ams3.cdn.digitaloceanspaces.com/similar_images/1/adc/7436c0d6739c6e1bc15efd6881455c156f98c.jpeg",
              "similarity": 0.682,
              "url_small": "https://crop-health.ams3.cdn.digitaloceanspaces.com/similar_images/1/adc/7436c0d6739c6e1bc15efd6881455c156f98c.small.jpeg"
            }
          ],
          "details": {
            "language": "en",
            "entity_id": "2746768c8d99bfbb"
          },
          "scientific_name": "Solanum tuberosum"
        }
      ]
    }
  },
  "status": "COMPLETED",
  "sla_compliant_client": True,
  "sla_compliant_system": True,
  "created": 1709893632.887534,
  "completed": 1709893633.628719
}

all_predictions = []
all_predictions.append(dict(RESPONSE))  # extracts values as predictions

highest_probability_prediction = CropInfo.get_top_prediction(all_predictions)

crop_name = CropInfo.get_top_crop_name(highest_probability_prediction)
crop_names = CropInfo.get_all_crop_names(highest_probability_prediction)
disease_name = CropInfo.get_top_disease_name(highest_probability_prediction)
disease_names = CropInfo.get_all_disease_names(highest_probability_prediction)

scientific_crop_name = CropInfo.get_top_crop_name(highest_probability_prediction, True)
scientific_crop_names = CropInfo.get_all_crop_names(highest_probability_prediction, True)
scientific_disease_name = CropInfo.get_top_disease_name(highest_probability_prediction, True)
scientific_disease_names = CropInfo.get_all_disease_names(highest_probability_prediction, True)

# print(highest_probability_prediction)

results_text = f"Crop Found!\n   Crop Name: {crop_name}\n   Disease Name: {scientific_disease_name}"
print(results_text)

print(f"Crop Name: {crop_name}")
print(f"Crop Names: {crop_name}")
print(f"Disease Name: {disease_name}")
print(f"Disease Names: {disease_names}")
print(f"Scientific Crop Name: {scientific_crop_name}")
print(f"Scientific Crop Names: {scientific_crop_name}")
print(f"Scientific Disease Name: {scientific_disease_name}")
print(f"Scientific Disease Names: {scientific_disease_names}")