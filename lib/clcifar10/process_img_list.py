s = open("img_list.txt", "r").readlines()
outfile = open("new_img_list.txt", "w")
for i in range(10):
    head = s[i*1001].rstrip().split('/')[1][:-1]
    for j in range(1000):
        print(head + '/' + s[i*1001+j].rstrip(), file=outfile)