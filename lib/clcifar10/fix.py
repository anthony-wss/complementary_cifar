import pandas as pd

df = pd.read_csv("10000_results.csv")
outfile = open("fix.csv", "w")

CATEGORIES = ["airplane", "automobile", "truck", "bird", "deer", "dog", "cat", "ship", "horse", "frog"]
img_list = [s.rstrip() for s in open("img_list.txt", "r").readlines()]
fix_imgs = [s.rstrip() for s in open("fix_img_list.txt", "r").readlines()]

print(len(df))

print("image_url_1,choice_1_1,choice_1_2,choice_1_3,choice_1_4,image_url_2,choice_2_1,choice_2_2,choice_2_3,choice_2_4,image_url_3,choice_3_1,choice_3_2,choice_3_3,choice_3_4,image_url_4,choice_4_1,choice_4_2,choice_4_3,choice_4_4,image_url_5,choice_5_1,choice_5_2,choice_5_3,choice_5_4,image_url_6,choice_6_1,choice_6_2,choice_6_3,choice_6_4,image_url_7,choice_7_1,choice_7_2,choice_7_3,choice_7_4,image_url_8,choice_8_1,choice_8_2,choice_8_3,choice_8_4,image_url_9,choice_9_1,choice_9_2,choice_9_3,choice_9_4,image_url_10,choice_10_1,choice_10_2,choice_10_3,choice_10_4", file=outfile)

for idx, row in df.iterrows():
    for i in range(10):
        if len(row[f'Input.image_url_{i+1}'].split('/')) == 3:
            s = ""
            for j in range(10):
                if len(row[f'Input.image_url_{j+1}'].split('/')) == 3:
                    cate = row[f'Input.image_url_{j+1}'].split('/')[0]
                    for img in fix_imgs:
                        if img.split('/')[0] == cate:
                            s += img + ","
                else:
                    s += row[f'Input.image_url_{j+1}'] + ","
                for k in range(4):
                    s += row[f"Input.choice_{j+1}_{k+1}"] + ","
            print(s[:-1], file=outfile)