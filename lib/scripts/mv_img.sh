# copy all 5000+1000 img of each category from train/ and test/ to all_data/

# for cate in "airplane" "automobile" "bird" "cat" "deer" "dog" "frog" "horse" "ship" "truck"; do
#     for i in {0..4999}; do
#         idx=$(printf "%04d" $i)
#         cp CIFAR-10-images/train/$cate/$idx.jpg CIFAR-10-images/all_data/$cate/$idx.jpg
#     done
# done

# for cate in "airplane" "automobile" "bird" "cat" "deer" "dog" "frog" "horse" "ship" "truck"; do
#     j=5000
#     for i in {0..999}; do
#         idx=$(printf "%04d" $i)
#         idx2=$(printf "%04d" $(($i+$j)))
#         cp CIFAR-10-images/test/$cate/$idx.jpg CIFAR-10-images/all_data/$cate/$idx2.jpg
#     done
# done

# Randomly sample 60 non-repeating img out of 6000 images
for cate in "airplane" "automobile" "bird" "cat" "deer" "dog" "frog" "horse" "ship" "truck"; do
    declare -a appeared
    for i in {0..5999}; do
        appeared[i]=0
    done
    for i in {0..179}; do
        r=$(( RANDOM % 6000 ))
        while [[ ${appeared[$r]} == 1 ]] ; do
            r=$(( RANDOM % 6000 ))
        done
        appeared[$r]=1
        idx=$(printf "%04d" $r)
        idx2=$(printf "%04d" $i)
        cp ../CIFAR-10-images/all_data/$cate/$idx.jpg images/$cate-$idx.jpg
    done
done