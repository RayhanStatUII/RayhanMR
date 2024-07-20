from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)  # Ganti _name_ dengan __name__

# Load the model
model = joblib.load('decision_tree_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    return jsonify(prediction.tolist())

if __name__ == '__main__':  # Ganti _name_ dengan __name__
    app.run(debug=True)
