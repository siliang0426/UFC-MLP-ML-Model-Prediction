from flask import Flask, request, jsonify
import torch
from model import MultiLayerPerceptronModel

app = Flask(__name__)

#hyper-parameter
input_size = 91
hidden_size = 256
output_size = 1
epoch = 70
dropout_rate = 0.4


model = torch.load('model.pth')
model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Convert data to tensor
    input_tensor = torch.tensor(data['input'])
    # Get prediction
    with torch.no_grad():
        prediction = model(input_tensor)
    # Convert prediction to response
    response = {'prediction': prediction.tolist()}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
