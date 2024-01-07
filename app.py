from flask import Flask, render_template, request    
#import joblib
import pickle
import numpy as np

app = Flask(__name__)
#model = joblib.load('heart_pickle.pkl')

with open('heart_pickle.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')    # Homepage indicated by /
def home():
    return render_template('index.html')   #parsing the html file

@app.route('/predict', methods=['POST'])
def predict():
    gender = request.form['gender']
    if gender == "Female":
        gender = 0
    elif gender == "Male":
        gender = 1
    else:
        gender = 2
    Hypertension = request.form['Hypertension']
    if Hypertension == "No":
        Hypertension = 0
    else:
        Hypertension =1
        
    HeartDisease = request.form['HeartDisease']
    if HeartDisease == "No":
        HeartDisease = 0
    else:
        HeartDisease =1

    everMarried = request.form['everMarried']
    if everMarried == "No":
        everMarried = 0
    else:
        everMarried =1

    workType = request.form['workType']
    if workType ==  "children":
        workType = 4

    if workType ==  "govt_job":
        workType = 0

    if workType ==  "never worked":
        workType = 1

    if workType ==  "private":
        workType = 2

    if workType ==  "self employed":
        workType = 3

    residenceType = request.form['residenceType']
    if workType ==  "Urban":
        workType = 1

    if workType ==  "Rural":
        workType = 0
        
    residenceType = request.form['residenceType']
    if residenceType == "Urban":  
        residenceType = 1
    else:
        residenceType = 0
        
    glucoseLevel = float(request.form['glucoseLevel'])  
    BMI = float(request.form['BMI'])  
    age = float(request.form['age']) 
 
    
    final = [gender, age, Hypertension, HeartDisease, everMarried, workType, residenceType, glucoseLevel, BMI]
    float_features = [float(x) for x in final]
    test_vector = np.reshape(np.asarray(float_features), (1, 9))
    print(test_vector)
    
    p = np.array(model.predict(test_vector))[0] 

    if p == 1:  
        pred = "There is a chance of stroke for this patient"
    else:
        pred = "There is no chance of stroke for this patient"

    return pred

if __name__ == "__main__":
    app.run(debug=True)  #Debug set to true to keep the server running and reflect changes on running
