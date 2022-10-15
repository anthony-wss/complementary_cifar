def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

s = """aquatic_mammals: 4, 30, 55, 72, 95
fish: 1, 32, 67, 73, 91
flowers: 54, 62, 70, 82, 92
food_containers: 9, 10, 16, 28, 61
fruit, vegetables and mushrooms: 0, 51, 53, 57, 83
household electrical devices: 22, 39, 40, 86, 87
household furniture: 5, 20, 25, 84, 94
insects: 6, 7, 14, 18, 24
large carnivores and bear: 3, 42, 43, 88, 97
large man-made outdoor things: 12, 17, 37, 68, 76
large natural outdoor scenes: 23, 33, 49, 60, 71
large omnivores and herbivores: 15, 19, 21, 31, 38
medium-sized mammals: 34, 63, 64, 66, 75
non-insect invertebrates: 26, 45, 77, 79, 99
people: 2, 11, 35, 46, 98
reptiles: 27, 29, 44, 78, 93
small mammals: 36, 50, 65, 74, 80
trees: 47, 52, 56, 59, 96
transportation vehicles: 8, 13, 48, 58, 90, 81
other vehicles: 41, 69, 85, 89"""
coarse_sub = [[int(n) for n in a.split(':')[1].split(',')] for a in s.split('\n')]
super_classes = [a.split(':')[0] for a in s.split('\n')]

outfile = open("select.html", "w")

header = """<style>
.row {
    display: flex;
}
.column {
    float: left;
}
.left {
    width: 75%;
}
.right {
    width: 25%;
}
.title {
    padding-top: 0px;
    margin-top: 30px;
    margin-right: 20px;
}
.wrapper {
  height: 50px;
  background-color: lightblue;
  display: flex;
  padding-left: 20px;
  align-items: center;
  margin-top: 20px;
}
.selection {
  height: 400px;
}
.choice {
  margin-top: 7px;
  margin-bottom: 7px;
  display: flex;
  flex-direction: row;
}
.choice_name {
  font-size: 14pt;
  width: 330px;
  padding-top: 10px;
  margin-right: 5px;
  margin-top: 10px;
  margin-bottom: 10px;
  background-color: lightgray;
}
.eg {
  font-size: 14pt;
  padding-top: 20px;
  padding-right: 3px;
}
</style>
<div class="row">
  <div class="column left" style="border-right:1px solid black;">"""

metadata = unpickle("cifar-100-python/meta")
trainset = unpickle("cifar-100-python/train")
filenames = [s.decode('utf-8') for s in trainset[b'filenames']]
coarse_label_names = [s.decode('utf-8') for s in metadata[b'coarse_label_names']]

print(header, file=outfile)

for i in range(1, 11):
    print(f"""
    <div id="p{i}" height=30px>
    </div>
    <div>
      <p class="title wrapper"> Problem {i}</p>
      <img src="https://cll-data-collect.s3.us-west-2.amazonaws.com/cifar100-large/${{image_url_{i}}}" height="200px"/>
      <p>
        Choose any one <span style="color: red;">"incorrect"</span> label for this image:
      </p>
      <div class="selection">""", file=outfile)
    for j in range(1, 5):
        print(
    f"""            <label class="choice">
      <div class="choice_name">
        <input type="radio" name="${{image_url_{i}}}" value="${{choice_{i}_{j}}}" required>
        ${{choice_{i}_{j}}}
      </div>
      <div class="eg">
        e.g.
      </div>
      <div>
        <img src="https://cll-data-collect.s3.us-west-2.amazonaws.com/sample_icon/${{sample_img_{i}_{j}}}">
      </div>
    </label>""", file=outfile)
    print(f"""      </div>
    </div>""", file=outfile)

print(f"""<div class="column right" style="position:fixed; top:0; right:0; padding-top: 20px;">
    <div style="padding-left: 5px">
    Links to all the problems:<br>
    <a href="#p1">problem 1</a><br>
    <a href="#p2">problem 2</a><br>
    <a href="#p3">problem 3</a><br>
    <a href="#p4">problem 4</a><br>
    <a href="#p5">problem 5</a><br>
    <a href="#p6">problem 6</a><br>
    <a href="#p7">problem 7</a><br>
    <a href="#p8">problem 8</a><br>
    <a href="#p9">problem 9</a><br>
    <a href="#p10">problem 10</a>
    </div>
  </div>
</div>""", file=outfile)

