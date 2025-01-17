from back_end.crop_info import CropInfo

RESPONSE = {
    "access_token": "SChIQy84K8bvPtd",
    "model_version": "crop_health:1.1.1",
    "custom_id": None,
    "input": {
        "latitude": 49.207,
        "longitude": 16.608,
        "similar_images": True,
        "images": [
            "https://crop.kindwise.com/media/images/1a5f0849a5d34a39add96afe60c75d0b.jpg"
        ],
        "datetime": "2024-03-13T09:42:15.948778+00:00"
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
                        "common_names": [
                            "Late Blight Of Potato",
                            "Downy Mildew Of Potato",
                            "Late Blight Of Tomato",
                            "Potato Blight"
                        ],
                        "type": "chromista",
                        "taxonomy": {
                            "class": "Oomycetes",
                            "genus": "Phytophthora",
                            "order": "Peronosporales",
                            "family": "Peronosporaceae",
                            "phylum": "Oomycota",
                            "kingdom": "Chromista"
                        },
                        "gbif_id": 3203716,
                        "eppo_code": "PHYTIN",
                        "eppo_regulation_status": {
                            "Chile": "A1 list",
                            "Guinea": "Regulated non-quarantine pest",
                            "Mexico": "Quarantine pest",
                            "Bahrain": "A2 list"
                        },
                        "wiki_url": "https://en.wikipedia.org/wiki/Phytophthora_infestans",
                        "wiki_description": {
                            "value": "Phytophthora infestans is an oomycete or water mold, a fungus-like microorganism that causes the serious potato and tomato disease known as late blight or potato blight. Early blight, caused by Alternaria solani, is also often called \"potato blight\". Late blight was a major culprit in the 1840s European, the 1845–1852 Irish, and the 1846 Highland potato famines. The organism can also infect some other members of the Solanaceae. The pathogen is favored by moist, cool environments: sporulation is optimal at 12–18 °C (54–64 °F) in water-saturated or nearly saturated environments, and zoospore production is favored at temperatures below 15 °C (59 °F). Lesion growth rates are typically optimal at a slightly warmer temperature range of 20 to 24 °C (68 to 75 °F).",
                            "citation": "https://en.wikipedia.org/wiki/Phytophthora_infestans",
                            "license_name": "CC BY-SA 3.0",
                            "license_url": "https://creativecommons.org/licenses/by-sa/3.0/"
                        },
                        "image": {
                            "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/wikidata/f87/f873d92e05a2a4f1aecf18da533b7192e5494d5f.jpg",
                            "citation": "//commons.wikimedia.org/wiki/User:Fk",
                            "license_name": "CC BY 2.5",
                            "license_url": "https://creativecommons.org/licenses/by/2.5/"
                        },
                        "images": [
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/wikipedia/724/724fe78530173153c5229425e421d67e2735c242.jpg",
                                "citation": "http://www.forestryimages.org/browse/detail.cfm?imgnum=5362902",
                                "license_name": "CC BY 3.0",
                                "license_url": "https://creativecommons.org/licenses/by/3.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/inaturalist/ea2/ea22aaeb4113eafb07967b0dafc57ce187ab2e7a.jpg",
                                "citation": "Rasbak",
                                "license_name": "CC BY-SA 4.0",
                                "license_url": "https://creativecommons.org/licenses/by-sa/4.0/"
                            }
                        ],
                        "description": "Late blight is a destructive plant disease caused by Phytophthora infestans, a type of water-mold species. It is highly aggressive and can cause significant crop loss. This disease was responsible for the historic Irish Potato Famine in the mid-19th century. P. infestans primarily affects the Solanaceous plants, commonly potato and tomato crops. The pathogen thrives in cool, damp weather conditions, and spreads rapidly via windborne spores. It can also survive in infected plant debris, making it a challenging and enduring threat to agricultural communities worldwide.",
                        "symptoms": {
                            "Wilting": " Despite adequate watering, plants may wilt as the disease obstructs water flow within the plant.",
                            "Shriveled fruit": " Infected fruit, such as tomatoes, may develop irregularly shaped, brown, greasy spots.",
                            "Rotting potatoes": " Infected potatoes display a reddish-brown decay, which often starts at the surface and extends into the tuber.",
                            "Leaf discoloration": " The plant's leaves start showing spots of greenish-black color, indicating an infection.",
                            "Reduction in yield": " Late Blight can significantly reduce plant productivity and yield.",
                            "White fuzzy growth": " On the underside of the leaves, a white fuzzy growth may be visible, especially during moist conditions.",
                            "Change in leaf color": " Infected leaves often turn brown and fall off, starting from the lower leaves.",
                            "Brown lesions on stem": " Brown or black lesions may appear on the stems, which could spread, making it wilty or shriveled.",
                            "Water-soaked appearance": " Infected areas on the leaves often appear \"water-soaked\" or oily.",
                            "Rapid collapse of the plant": " The disease can cause plant tissues to rapidly collapse and decay."
                        },
                        "severity": "This devastating plant disease poses a massive threat to the health of crops. It is particularly known for affecting the grow-stage of a plant cycle, causing severe and irreparable damage to leaves, stems, and fruits. In many cases, it can lead to complete crop failure if left unchecked. It strikes the optimal growth period of plants making it highly dangerous to yield production.",
                        "spreading": "This plant disease spreads primarily through airborne spores, which can travel considerable distances, infecting crops even miles away. Wet, humid conditions highly favor its rampant spread, and under these conditions, it can devastate an entire field in as little as one week. Cool temperatures ranging between 12°C (53.6°F) and 24°C (75.2°F) also encourage its proliferation, and even the smallest spore can potentially create thousands more, accelerating its spread. The disease can also spread through infected plant material and contaminated soil or equipment.",
                        "treatment": {
                            "prevention": [
                                "Regular field monitoring: Inspect your crops routinely for early detection and control of late blight.",
                                "Removal and destruction of infected plants: Always remove and destroy the infected plants immediately to prevent the spread of disease.",
                                "Use certified seed: Always use seed tubers that are certified disease-free.",
                                "Crop rotation: Involve in crop rotation with non-host crops to disrupt the disease cycle.",
                                "Adequate spacing: Ensure sufficient spacing between plants to promote air circulation reducing conditions favouring the disease."
                            ],
                            "chemical treatment": [
                                "Use of Fungicides: Apply fungicides such as copper or chlorothalonil for effective control of late blight.",
                                "Systemic fungicides application: Use systemic fungicides like Ridomil Gold, which are absorbed by the plant and can control the disease.",
                                "Treatment with specific anti-oomycete chemicals: Use chemicals like mefenoxam and dimethomorph specialized in combating organisms like P. infestans.",
                                "Timely chemical sprays: Provide regular chemical sprays particularly Before rainy periods.",
                                "Post-harvest treatment: Use post-harvest treatments like Phostrol to slow down the disease growth in stored crops."
                            ],
                            "biological treatment": [
                                "Introduction of predatory organisms: Introduce beneficial organisms such as Trichoderma species which are known to combat Phytophthora infestans.",
                                "Application of biofungicides: Apply biofungicides like Serenade, which contain Bacillus subtilis strain QST 713, known to suppress P. infestans.",
                                "Composting infected plant tissues: Properly compost all infected plant tissues to kill the blight pathogens.",
                                "Exploitation of plant resistance: Utilise late-blight resistant plant species or cultivars to reduce disease incidence.",
                                "Soil solarization: Implement soil solarization in affected areas to kill the blight in the soil during the hottest months."
                            ]
                        },
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
                        "common_names": None,
                        "type": "abiotic",
                        "taxonomy": None,
                        "gbif_id": None,
                        "eppo_code": None,
                        "eppo_regulation_status": None,
                        "wiki_url": None,
                        "wiki_description": None,
                        "image": None,
                        "images": None,
                        "description": None,
                        "symptoms": None,
                        "severity": None,
                        "spreading": None,
                        "treatment": None,
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
                    "probability": 0.8749,
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
                        "gbif_id": 2930262,
                        "image": {
                            "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/wikidata/164/16432620b1385d2fc023e391fc28d82c3fe58f01.jpg",
                            "citation": "https://commons.wikimedia.org/wiki/File:Potato_sprout,_January_23,_2006.jpg",
                            "license_name": "CC BY-SA 2.0",
                            "license_url": "https://creativecommons.org/licenses/by-sa/2.0/"
                        },
                        "images": [
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/wikidata/9e9/9e97856b76392de7da2f34dc5378a4be7acb75a3.jpg",
                                "citation": "http://www.hear.org/starr/",
                                "license_name": "CC BY 3.0",
                                "license_url": "https://creativecommons.org/licenses/by/3.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/wikidata/3f7/3f7d894c01fec1133fc0e1acb9ec231e0eba24c6.jpg",
                                "citation": None,
                                "license_name": "CC0",
                                "license_url": "https://creativecommons.org/publicdomain/zero/1.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/wikidata/c3f/c3f5fa09ee01db021ce5e434881e8472a735abda.jpg",
                                "citation": None,
                                "license_name": "CC0",
                                "license_url": "https://creativecommons.org/publicdomain/zero/1.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/wikipedia/e16/e16754869b0b28552932959241be2e90b9025e94.jpg",
                                "citation": "Dodo",
                                "license_name": "CC0",
                                "license_url": "https://creativecommons.org/publicdomain/zero/1.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/inaturalist/16d/16d124aad221bad4b7fc10cc7d5ffc726296bff4.jpeg",
                                "citation": "Andres Casas Ponce",
                                "license_name": "CC0",
                                "license_url": "https://creativecommons.org/publicdomain/zero/1.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/inaturalist/037/037aab3f52354a11965d7ac6ca3280985a498171.jpeg",
                                "citation": "Veronika H.",
                                "license_name": "CC0",
                                "license_url": "https://creativecommons.org/publicdomain/zero/1.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/gbif/8c4/8c424e41dcf5725fd5bd5b357e27dfd05b36f6be.jpeg",
                                "citation": "https://www.inaturalist.org/photos/177228436",
                                "license_name": "CC BY-SA 4.0",
                                "license_url": "https://creativecommons.org/licenses/by-sa/4.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/gbif/25e/25e49c22d5d1b3a672020860e70efff2690733ca.jpeg",
                                "citation": "https://www.gbif.org/occurrence/3949367831",
                                "license_name": "CC BY 4.0",
                                "license_url": "https://creativecommons.org/licenses/by/4.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/gbif/cd9/cd937383fdaa23e925605999c54182455ef0fefb.jpeg",
                                "citation": "https://www.inaturalist.org/photos/178266257",
                                "license_name": "CC0",
                                "license_url": "https://creativecommons.org/publicdomain/zero/1.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/gbif/729/729ee8badc50f4c1dbb52007050f511cf4b47076.jpeg",
                                "citation": "https://www.inaturalist.org/photos/178266242",
                                "license_name": "CC0",
                                "license_url": "https://creativecommons.org/publicdomain/zero/1.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/gbif/5be/5be9355aacebce451965d4d716c30d65fb14baba.jpeg",
                                "citation": "https://www.inaturalist.org/photos/178293980",
                                "license_name": "CC BY 4.0",
                                "license_url": "https://creativecommons.org/licenses/by/4.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/gbif/377/377ad14ba65aea03538c81d46807f294071ca409.jpeg",
                                "citation": "https://www.inaturalist.org/photos/178294013",
                                "license_name": "CC BY 4.0",
                                "license_url": "https://creativecommons.org/licenses/by/4.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/gbif/c17/c171dd8b2a2ef381d5ead20bc1ddd23f40ad7d40.jpeg",
                                "citation": "https://www.inaturalist.org/photos/179097110",
                                "license_name": "CC BY 4.0",
                                "license_url": "https://creativecommons.org/licenses/by/4.0/"
                            },
                            {
                                "value": "https://crop-health.ams3.cdn.digitaloceanspaces.com/knowledge_base/gbif/e76/e76e2c89da48fc84aa0974cbc45b5c1b88730667.jpeg",
                                "citation": "https://www.inaturalist.org/photos/179097109",
                                "license_name": "CC BY 4.0",
                                "license_url": "https://creativecommons.org/licenses/by/4.0/"
                            }
                        ],
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
    "created": 1710322935.948778,
    "completed": 1710322936.674678
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