from flask import Flask, render_template, request, session
from flask_session import Session
import pandas as pd
app = Flask(__name__)
alist=["one","two"]
#app.config["SESSION_PERMANENT"]=False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

@app.route("/")
def index():
    return (f"Helo changed. File name:{__name__}")

@app.route("/this")
def indexx():
    return("Thisisjk")

@app.route("/<string:name>")
def hello(name):    
    return render_template("index.html",yourName=name,hd="Yoo") 

@app.route("/temp")
def indexxx():
    hd = " What is this?"
    return render_template("index.html",hd=hd)

@app.route("/helloo",methods=["POST"])
def helloo():
    name = request.files["name"]    
    try:
        df = pd.read_csv(name)
        
    except :
        print("Error")
        pass
    
    #session["alist"].append(name)    
    return render_template("index.html",hd="Redirected", values = df,
    tableheads=df.columns ,alist=df.iloc[0])
    # session.get("alist"))