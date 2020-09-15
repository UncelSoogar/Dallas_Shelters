from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
import pickle
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
import os


app = Flask(__name__)

#Import scalers and models
filename = 'static/models/cat_scaler.sav'
infile = open(filename,'rb')
cat_scaler = pickle.load(infile)
infile.close()

filename = 'static/models/cat_model.sav'
infile = open(filename,'rb')
cat_model = pickle.load(infile)
infile.close()

filename = 'static/models/dog_scaler.sav'
infile = open(filename,'rb')
dog_scaler = pickle.load(infile)
infile.close()

filename = 'static/models/dog_model.sav'
infile = open(filename,'rb')
dog_model = pickle.load(infile)
infile.close()
Bootstrap(app)


#ROUTES FOR PAGES

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about_us():
    return render_template('about.html')

@app.route('/dash_cat')
def dash_cat():
    return render_template('dash_cat.html')

@app.route('/dash_dog')
def dash_dog():
    return render_template('dash_dog.html')

@app.route('/dash_main')
def dash_main():
    return render_template('dash_main.html')

@app.route('/methodology')
def methodology():
    return render_template('methodology.html')

@app.route('/cat_predictions')
def cat_predicionts():   
    return render_template('cat_predictions.html')

@app.route('/dog_predictions')
def dog_predicionts():   
    return render_template('dog_predictions.html')


@app.route('/cat_predict', methods=['POST'])
def cat_predict():
    if request.method =='POST':
        #Retrieve from values
        cat_breed = request.form['cat_breed']
        cat_origin = request.form['cat_origin']
        cat_chip = request.form['cat_chip']
        cat_intake = request.form['cat_intake']
        cat_days = request.form['cat_days']

        #Use form values to create list for model
        #variables to use in model values
        los = 0 
        lh = 0
        mh= 0
        sh = 0
        field = 0
        counter = 0
        chip = 0 
        nochip = 0
        noscan = 0 
        contagious = 0
        healthy = 0
        manageable = 0
        rehab = 0
        untreat = 0

        #if else for breed values
        if cat_breed == "Short Hair":
            sh = 1
        elif cat_breed == "Medium Hair":
            mh = 1
        else:
            lh = 1

        #if else for origin values
        if cat_origin == "Field":
            field = 1
        else:
            counter = 1

        #if else for chip values
        if cat_chip == "Chip":
            chip = 1
        elif cat_chip == "No Chip":
            nochip = 1
        else:
            noscan = 1

        #if else for intake
        if cat_intake == "Healthy":
            healthy = 1
        elif cat_intake == "Contagious":
            contagious = 1
        elif cat_intake == "Rehabilitable, Non-Contagious":
            rehab = 1
        elif cat_intake == "Manageable, Non-Contagious":
            manageable = 1
        else:
            untreat =1

        #convert cat_days to int. Return error to user if wrong input typed
        try:
            los = int(cat_days)
        except(ValueError):
            cat_days = "INTEGERS ONLY"


        #Create a cat using values from user
        test_cat = [[los, lh, mh, sh, field, counter, chip, nochip, noscan, contagious, healthy, manageable, rehab, untreat]]



        #scale cat
        test_cat = cat_scaler.transform(test_cat)

        #model cat
        cat_result = cat_model.predict(test_cat)

        #change result to meaningful outcome
        if cat_result== 0:
            cat_result = "adopted!"
            cat_img = 'static/imgs/cat_adopt.jpg'
        elif cat_result == 1:
            cat_result = "euthanized."
            cat_img = 'static/imgs/cat_euth.jpg'
        elif cat_result == 2:
            cat_result = "returned to owner"
            cat_img = 'static/imgs/pet_own.jpg'
        else:
            cat_result = "transfered or fostered"
            cat_img = "static/imgs/cat_trans.jpg"

        #probs
        cat_probs = cat_model.predict_proba(test_cat)
        adopt_probs = f'{round(cat_probs[0][0], 2) *100}%'
        euth_probs = f'{round(cat_probs[0][1], 2) *100}%'
        owner_probs = f'{round(cat_probs[0][2], 2) *100}%'
        trans_probs = f'{round(cat_probs[0][3], 2) *100}%'

        return render_template('cat_predictions.html', cat_breed = cat_breed, cat_origin = cat_origin,
         cat_chip = cat_chip, cat_intake = cat_intake, cat_days = cat_days, cat_result = cat_result,
         adopt_probs = adopt_probs, euth_probs =euth_probs, owner_probs = owner_probs, trans_probs = trans_probs, cat_img = cat_img)



@app.route('/dog_predict', methods=['POST'])
def dog_predict():
    if request.method =='POST':
        #Retrieve from values
        dog_breed = request.form['dog_breed']
        dog_origin = request.form['dog_origin']
        dog_chip = request.form['dog_chip']
        dog_intake = request.form['dog_intake']
        dog_days = request.form['dog_days']

        #Use form values to create list for model
        #variables to use in model values

        los = 0 
        chihuahua = 0
        corgi= 0
        hound = 0
        other = 0
        pitbull = 0
        pug = 0
        retriever = 0
        shepherd = 0
        terrier = 0
        field = 0
        counter = 0
        chip = 0 
        nochip = 0
        noscan = 0 
        contagious = 0
        healthy = 0
        manageable = 0
        rehab = 0
        untreat = 0

        #if else for breed values
        if dog_breed == "Chihuahua":
            chihuahua = 1
        elif dog_breed == "Corgi":
            corgi = 1
        elif dog_breed == "Hound":
            hound = 1
        elif dog_breed == "Other":
            other = 1
        elif dog_breed == "Pitbull":
            pitbull = 1
        elif dog_breed == "Pug":
            pug = 1
        elif dog_breed == "Retriever":
            retriever = 1
        elif dog_breed == "Shepherd":
            shepherd = 1
        else:
            terrier = 1

        #if else for origin values
        if dog_origin == "Field":
            field = 1
        else:
            counter = 1

        #if else for chip values
        if dog_chip == "Chip":
            chip = 1
        elif dog_chip == "No Chip":
            nochip = 1
        else:
            noscan = 1

        #if else for intake
        if dog_intake == "Healthy":
            healthy = 1
        elif dog_intake == "Contagious":
            contagious = 1
        elif dog_intake == "Rehabilitable, Non-Contagious":
            rehab = 1
        elif dog_intake == "Manageable, Non-Contagious":
            manageable = 1
        else:
            untreat =1

        #convert dog_days to int. Return error to user if wrong input typed
        try:
            los = int(dog_days)
        except(ValueError):
            dog_days = "INTEGERS ONLY"


        #Create a dog using values from user
        test_dog = [[los, chihuahua, corgi, hound, other, pitbull, pug, retriever, shepherd, terrier, field, counter, chip, nochip, noscan, contagious, healthy, manageable, rehab, untreat]]

        #scale dog
        test_dog = dog_scaler.transform(test_dog)

        #model dog
        dog_result = dog_model.predict(test_dog)

        #change result to meaningful outcome
        if dog_result== 0:
            dog_result = "adopted!"
            dog_img = 'static/imgs/dog_adopt.jpg'
        elif dog_result == 1:
            dog_result = "euthanized."
            dog_img = 'static/imgs/dog_euth.jpg'
        elif dog_result == 2:
            dog_result = "returned to owner."
            dog_img = 'static/imgs/pet_own.jpg'
        else:
            dog_result = "transfered or fostered."
            dog_img = "static/imgs/dog_trans.jpg"

        #probs
        dog_probs = dog_model.predict_proba(test_dog)
        adopt_probs = f'{round(dog_probs[0][0], 2) *100}%'
        euth_probs = f'{round(dog_probs[0][1], 2) *100}%'
        owner_probs = f'{round(dog_probs[0][2], 2) *100}%'
        trans_probs = f'{round(dog_probs[0][3], 2) *100}%'

        return render_template('dog_predictions.html', dog_breed = dog_breed, dog_origin = dog_origin,
         dog_chip = dog_chip, dog_intake = dog_intake, dog_days = dog_days, dog_result = dog_result,
         adopt_probs = adopt_probs, euth_probs =euth_probs, owner_probs = owner_probs, trans_probs = trans_probs, dog_img = dog_img)

if __name__ == '__main__':
    app.run(debug=True)
