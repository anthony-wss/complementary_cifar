import json

obj = json.loads("""[{"image_1":{"automobile-3":true,"deer-4":false,"dog-1":false,"ship-2":false},"image_10":{"airplane-1":true,"frog-3":false,"horse-4":false,"truck-2":false},"image_2":{"airplane-1":false,"automobile-4":false,"frog-2":false,"ship-3":true},"image_3":{"cat-2":true,"dog-4":false,"frog-1":false,"truck-3":false},"image_4":{"airplane-2":false,"cat-1":true,"frog-4":false,"ship-3":false},"image_5":{"automobile-1":false,"cat-4":false,"dog-2":true,"horse-3":false},"image_6":{"airplane-3":true,"automobile-2":false,"dog-4":false,"ship-1":false},"image_7":{"automobile-1":true,"deer-4":false,"dog-2":false,"truck-3":false},"image_8":{"airplane-4":true,"bird-2":false,"cat-1":false,"truck-3":false},"image_9":{"airplane-3":true,"bird-2":false,"deer-1":false,"frog-4":false}}]"""[1:-1])

for i in range(1, 11):
    true_cnt, false_cnt = 0, 0
    for k in obj[f"image_{i}"].values():
        if k:
            true_cnt += 1
        else:
            false_cnt += 1
    if true_cnt != 1 or false_cnt != 3:
        print("invalid")
    else:
        print("valid")
