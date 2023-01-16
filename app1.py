from flask import Flask, render_template, request

app = Flask(__name__)

def num_func(string):
    """Num func"""
    SUM = 0
    string = string.split()
    for nums in range(len(string)):
        string[nums] = int(string[nums])

    string = sorted(string)
    SUM = string[0] + string[1]
    return SUM

@app.route('/', methods=['GET', 'POST'])
def test():
    """function with flask"""
    result = ''
    if request.method == "POST":
        data = request.form.get("Data")
        result = num_func(data)
    return render_template("index.html", result=result)

if __name__== '__main__':
    app.run()