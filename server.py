# from turtle import color
from flask import Flask, render_template 
# from hello import repeat 
app = Flask(__name__)

@app.route("/play/<int:x>/<color>")
def play(x,color):
    # repeat(x)
    return render_template("index.html",x = x, color =color)


@app.route("/")
def welcome():
    return "Welcome to Flask"

if __name__ == '__main__':
    app.run(debug=True)