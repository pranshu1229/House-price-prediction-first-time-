from flask import Flask,render_template,request,redirect
# from sklearn.externals import joblib
# import sklearn.external.joblib as extjoblib

import joblib


app = Flask(__name__) 
model=joblib.load('model.pkl')

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/",methods=['POST']) 
def price(): 
    if request.method=="POST":
        age=float(request.form['age'])
        distance=float(request.form['distance'])
        number=float(request.form['number'])
        pred_price=str(model.predict([[age,distance,number]])[0][0])
    return render_template('index.html',price=pred_price)

	
if __name__=="__main__":
    app.run(debug=True,port=1229)