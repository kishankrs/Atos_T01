from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('sav_model.pkl', 'rb'))


@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    radius_mean = float(request.form['radius_mean'])
    texture_mean = float(request.form['texture_mean'])
    perimeter_mean = float(request.form['perimeter_mean'])
    area_mean = float(request.form['area_mean'])
    compactness_mean = float(request.form['compactness_mean'])
    concavity_mean = float(request.form['concavity_mean'])
    # possibility of error in concave points_mean
    concave_points_mean = float(request.form['concave_points_mean'])
    symmetry_mean = float(request.form['symmetry_mean'])
    radius_se = float(request.form['radius_se'])
    perimeter_se = float(request.form['perimeter_se'])
    area_se = float(request.form['area_se'])
    smoothness_se = float(request.form['smoothness_se'])
    compactness_se = float(request.form['compactness_se'])
    # possibility of error in concave points_se
    concave_points_se = float(request.form['concave_points_se'])
    symmetry_se = float(request.form['symmetry_se'])
    fractal_dimension_se = float(request.form['fractal_dimension_se'])
    radius_worst = float(request.form['radius_worst'])
    texture_worst = float(request.form['texture_worst'])
    perimeter_worst = float(request.form['perimeter_worst'])
    area_worst = float(request.form['area_worst'])
    smoothness_worst = float(request.form['smoothness_worst'])
    concavity_worst = float(request.form['concavity_worst'])
    # possibility of error in concave points_worst
    concave_points_worst = float(request.form['concave_points_worst'])
    symmetry_worst = float(request.form['symmetry_worst'])

    result = model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean,
                             compactness_mean, concavity_mean, concave_points_mean,
                             symmetry_mean, radius_se, perimeter_se, area_se,
                             smoothness_se, compactness_se, concave_points_se, symmetry_se,
                             fractal_dimension_se, radius_worst, texture_worst,
                             perimeter_worst, area_worst, smoothness_worst, concavity_worst,
                             concave_points_worst, symmetry_worst]])[0]

    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
