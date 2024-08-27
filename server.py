from flask import Flask
from flask import render_template
from flask import request
import model


app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")
  
@app.route("/result")
def result():
  return render_template("result.html")

if __name__ == "__main__":
  app.run()
