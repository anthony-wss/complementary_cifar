import json

s = """[{"aquatic_mammals/dolphin_s_001355.png":{"flowers":false,"household furniture":true,"insects":false,"non-insect invertebrates":false},"fish/halibut_s_000350.png":{"flowers":true,"food_containers":false,"fruit, vegetables and mushrooms":false,"trees":false},"fish/stingray_s_000581.png":{"large carnivores and bear":true,"large natural outdoor scenes":false,"non-insect invertebrates":false,"small mammals":false},"flowers/orchid_s_001818.png":{"food_containers":true,"fruit, vegetables and mushrooms":false,"large carnivores and bear":false,"trees":false},"food_containers/pill_bottle_s_000040.png":{"flowers":true,"large carnivores and bear":false,"reptiles":false,"transportation vehicles":false},"food_containers/soda_can_s_000094.png":{"aquatic_mammals":false,"flowers":true,"insects":false,"reptiles":false},"household_furniture/overstuffed_chair_s_000325.png":{"non-transportation vehicles":false,"people":false,"small mammals":true,"trees":false},"large_omnivores_and_herbivores/chimpanzee_s_000083.png":{"food_containers":true,"fruit, vegetables and mushrooms":false,"large carnivores and bear":false,"large omnivores and herbivores":false},"trees/oak_tree_s_001424.png":{"aquatic_mammals":false,"fruit, vegetables and mushrooms":true,"medium-sized mammals":false,"reptiles":false},"trees/quercus_robur_s_001499.png":{"fish":true,"household electrical devices":false,"insects":false,"non-insect invertebrates":false}}]"""[1:-1]

obj = json.loads(s)


for name in obj.keys():
    choices = obj[name].keys()
    valid = False
    for c in choices:
        if obj[name][c] is True:
            valid = True
    if valid is False:
        print("error!")
        exit()
print("accepted")