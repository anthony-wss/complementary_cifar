img_list = [s.rstrip() for s in open("../filenames_list.txt", "r").readlines()]
outfile = open("filenames_list_fix.txt", "w")

for i in range(len(img_list)):
    superclass, filename = img_list[i].split('/')
    if superclass == 'fruit_vegetables_and_mushrooms':
        superclass = 'fruit, vegetables and mushrooms'
    elif superclass == 'household_electrical_devices':
        superclass = 'household electrical devices'
    elif superclass == 'household_furniture':
        superclass = 'household furniture'
    elif superclass == 'large_carnivores_and_bear':
        superclass = 'large carnivores and bear'
    elif superclass == 'large_man-made_outdoor_things':
        superclass = 'large man-made outdoor things'
    elif superclass == 'large_natural_outdoor_scenes':
        superclass = 'large natural outdoor scenes'
    elif superclass == 'large_omnivores_and_herbivores':
        superclass = 'large omnivores and herbivores'
    elif superclass == 'medium-sized_mammals':
        superclass = 'medium-sized mammals'
    elif superclass == 'non-insect_invertebrates':
        superclass = 'non-insect invertebrates'
    elif superclass == 'transportation_vehicles':
        superclass = 'transportation vehicles'
    elif superclass == 'small_mammals':
        superclass = 'small mammals'
    elif superclass == 'other_vehicles':
        superclass = 'non-transportation vehicles'
    print(superclass+'/'+filename, file=outfile)