from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('sav_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    radius_mean = float(request['radius_mean'])
    texture_mean = float(request['texture_mean'])
    perimeter_mean = float(request['perimeter_mean'])
    area_mean = float(request['area_mean'])
    compactness_mean = float(request['compactness_mean'])
    concavity_mean = float(request['concavity_mean'])
    # possibility of error in concave points_mean
    concave_points_mean = float(request['concave points_mean'])
    symmetry_mean = float(request['symmetry_mean'])
    radius_se = float(request['radius_se'])
    perimeter_se = float(request['perimeter_se'])
    area_se = float(request['area_se'])
    smoothness_se = float(request['smoothness_se'])
    compactness_se = float(request['compactness_se'])
    # possibility of error in concave points_se
    concave_points_se = float(request['concave points_se'])
    symmetry_se = float(request['symmetry_se'])
    fractal_dimension_se = float(request['fractal_dimension_se'])
    radius_worst = float(request['radius_worst'])
    texture_worst = float(request['texture_worst'])
    perimeter_worst = float(request['perimeter_worst'])
    area_worst = float(request['area_worst'])
    smoothness_worst = float(request['smoothness_worst'])
    concavity_worst = float(request['concavity_worst'])
    # possibility of error in concave points_worst
    concave_points_worst = float(request['concave points_worst'])
    symmetry_worst = float(request['symmetry_worst'])

    result = model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean,
                             compactness_mean, concavity_mean, concave_points_mean,
                             symmetry_mean, radius_se, perimeter_se, area_se,
                             smoothness_se, compactness_se, concave_points_se, symmetry_se,
                             fractal_dimension_se, radius_worst, texture_worst,
                             perimeter_worst, area_worst, smoothness_worst, concavity_worst,
                             concave_points_worst, symmetry_worst]])[0]

    return render_template('index.html', **locals)


if __name__ == '__main__':
    app.run(debug=True)
