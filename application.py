# FIX: Import redirect, url_for, and session
from flask import Flask, request, render_template, redirect, url_for, session
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# FIX: Add a secret key to use the session
app.secret_key = 'your_super_secret_key'

## Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        # FIX: Get the result from the session if it exists
        # .pop() retrieves the value and removes it, so it only shows once
        results = session.pop('results', None)
        return render_template('home.html', results=results)
    else: # This is the POST request
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # FIX: Store the result in the session instead of rendering directly
        session['results'] = round(results[0], 2) # Rounding for a cleaner display

        # FIX: Redirect back to the same page (which will now be a GET request)
        return redirect(url_for('predict_datapoint'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")