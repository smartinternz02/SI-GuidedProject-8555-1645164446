import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import random

#import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
'''API_KEY = "Sq_Hu7yuAk_uDjRUF8o8lvs2qN2sL4XEUEtFrU2pJr6t"
token_response = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/6d1ca205-9b32-482c-86fc-b6aa5ae9ed50/predictions?version=2022-03-05', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
'''

app = Flask(__name__)
model = joblib.load("engine_model.sav")


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/m_predict',methods=['POST'])
def mpred():
    return render_template('Manual_predict.html')
@app.route('/s_predict',methods=['POST'])
def spred():
    return render_template('Sensor_predict.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    x_test = [[int(x) for x in request.form.values()]]
    
    
    print(x_test)
    a = model.predict(x_test)
    pred = a[0]
    if(pred == 0):
        pred = "No failure expected within 30 days."
    else:
        pred = "Maintenance Required!! Expected a failure within 30 days."
    
    return render_template('Manual_predict.html', prediction_text=pred)





if __name__ == '__main__':
    app.run(debug=False)
