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
    radius_mean = request['radius_mean']
    texture_mean = request['texture_mean']
    perimeter_mean = request['perimeter_mean']
    area_mean = request['area_mean']
    compactness_mean = request['compactness_mean']
    concavity_mean = request['concavity_mean']
    # possibility of error in concave points_mean
    concave_points_mean = request['concave points_mean']
    symmetry_mean = request['symmetry_mean']
    radius_se = request['radius_se']
    perimeter_se = request['perimeter_se']
    area_se = request['area_se']
    smoothness_se = request['smoothness_se']
    compactness_se = request['compactness_se']
    # possibility of error in concave points_se
    concave_points_se = request['concave points_se']
    symmetry_se = request['symmetry_se']
    fractal_dimension_se = request['fractal_dimension_se']
    radius_worst = request['radius_worst']
    texture_worst = request['texture_worst']
    perimeter_worst = request['perimeter_worst']
    area_worst = request['area_worst']
    smoothness_worst = request['smoothness_worst']
    concavity_worst = request['concavity_worst']
    # possibility of error in concave points_worst
    concave_points_worst = request['concave points_worst']
    symmetry_worst = request['symmetry_worst']


if __name__ == '__main__':
    app.run(debug=True)
