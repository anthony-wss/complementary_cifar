header = """
<!-- You must include this JavaScript file -->
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<!-- For the full list of available Crowd HTML Elements and their input/output documentation,
      please refer to https://docs.aws.amazon.com/sagemaker/latest/dg/sms-ui-template-reference.html -->

<!-- You must include crowd-form so that your task submits answers to MTurk -->
<style>
.question {
  display: flex;
  align-items: center;
  justify-content: space-around;
}
.image {
  margin-right: 10px;
}
.selection {
  flex: content;
}
.wrapper {
  height: 60px;
  background-color: lightblue;
  display: flex;
  padding-left: 20px;
  align-items: center;
  margin-top: 20px;
  margin-bottom: 10px;
}
.statement {
  height: 100px;
  background-color: rgba(229, 184, 167, 0.886);
  display: flex;
  padding-left: 20px;
  align-items: center;
  font-size: larger;
}
img {
  margin-bottom: 10px;
}
label {
  display: flex;
	cursor: pointer;
	font-weight: 400;
  font-size: larger;
  color: black;
	position: relative;
	overflow: hidden;
	margin-bottom: 0.175em;
  outline: .125em solid lightgray;
  background-color: lightgray;
  width: 150px;
}
input {
  position: relative;
  margin-top: 5px;
  margin-right: 5px;
}
</style>

<crowd-form>

<script>
  function updateCnt() {
    var inputs = document.getElementById("form").elements;
    var count  = 0;
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].type == 'radio' && inputs[i].checked) {
            count++;
        }
    }
    document.getElementById("cnt").innerHTML = count.toString();
  }
</script>

<div class="statement">
<p>Please select any <span style="color: red;">"incorrect one"</span> category for this image:</p>
</div>

<form id="form">

"""

footer = """

</form>

<div style="margin-bottom:2700px;"></div>
Total answered problems: <span id="cnt">0</span> / 10<br>
Note that you should answer <span style="color: red;">all the 10 problems</span>.<br>
</crowd-form>
"""

outfile = open("form.html", "w")

print(header, file=outfile)
for i in range(1, 10+1):
    print(f"""
    <div class="wrapper">
        <span>Problem {i}</span>
    </div>
    <div class="question">
        <div class="image">
        <img width="200px" src="https://cll-data-collect.s3.us-west-2.amazonaws.com/images/${{image_url_{i}}}">
        </div>
        <div class="selection">
        <label>
            <input type="radio" name="image_{i}" value="${{choice_{i}_1}}-1" onclick="updateCnt();">
            ${{choice_{i}_1}}
        </label><br>
    
        <label>
            <input type="radio" name="image_{i}" value="${{choice_{i}_2}}-2" onclick="updateCnt();">
            ${{choice_{i}_2}}
        </label><br>
    
        <label>
            <input type="radio" name="image_{i}" value="${{choice_{i}_3}}-3" onclick="updateCnt();">
            ${{choice_{i}_3}}
        </label><br>
    
        <label>
            <input type="radio" name="image_{i}" value="${{choice_{i}_4}}-4" onclick="updateCnt();">
            ${{choice_{i}_4}}
        </label><br>
        </div>
    </div>
    """, file=outfile)
print(footer, file=outfile)