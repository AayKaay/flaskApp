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

@app.route("/indexBase")
def indexBase():
    return render_template("indexBase.html")


@app.route("/")
def index():
    return (f"Hello World.. File name:{__name__}")

@app.route("/this")
def indexx():
    return("Thisisjk")

@app.route("/<string:name>")
def hello(name):    
    return render_template("error.html") 

@app.route("/temp")
def indexxx():
    return render_template("index.html")

@app.route("/helloo",methods=["POST","GET"])
def helloo():
    if request.method == "POST":     
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
    else:
        return ("Get Request dealt with.")