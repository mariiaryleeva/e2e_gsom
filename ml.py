from flask import Flask, request
import joblib
import numpy

MODEL_PATH = 'mlmodel/model.pkl'
SCALER_X_PATH = 'mlmodel/scaler_x.pkl'
SCALER_Y_PATH = 'mlmodel/scaler_y.pkl'

ml = Flask(__name__)

@ml.route('/predict_price', methods = ['GET'])
def predict():
    args = request.args
    open_plan = args.get('open_plan', default=-1, type=int)
    rooms = args.get('rooms', default=-1, type=int)
    area = args.get("area", default=-1, type=float)
    renovation = args.get('renovation', default=-1, type=int)

    # response = 'open_plan:{}, rooms:{}, area:{}, renovation:{}'.format(open_plan, rooms, area, renovation)
    model = joblib.load(MODEL_PATH)
    sc_x = joblib.load(SCALER_X_PATH)
    sc_y = joblib.load(SCALER_Y_PATH)

    x = numpy.array([open_plan, rooms, area, renovation]).reshape(1, -1)
    x = sc_x.transform(x)
    result = model.predict(x)
    result = sc_y.inverse_transform(result.reshape(1, -1))

    return str(result[0][0])


if __name__ == '__main__':
   ml.run(debug=True, port=5444, host='0.0.0.0')