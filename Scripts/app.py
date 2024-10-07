from flask import Flask, request, redirect
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd
import os
import prediction

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)


class GetPredictionOutput(Resource):
    def get(self):
        return {"error":"Invalid Method."}

    def post(self):
        try:
            data = request.get_json()
            predict = prediction.predict_mpg(data)
            predictOutput = predict
            return {'Prediction ': predictOutput}

        except Exception as error:
            return {'error': error}

api.add_resource(GetPredictionOutput,'/getPredictionOutput')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)