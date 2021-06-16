from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from FlaskApi.app import model

app = Flask(__name__)
CORS(app)

# 預設方法為 GET
@app.route('/predict',methods=['POST'])
def postInput():
    # 從前端獲取數值
    insertValues = request.get_json()
    # x1 = insertValues['sepalLengthCm']
    # x2 = insertValues['sepalWidthCm']
    # x3 = insertValues['petalLengthCm']
    # x4 = insertValues['petalWidthCm']

    x1= insertValues['Pregnancies']
    x2= insertValues['Glucose']
    x3= insertValues['BloodPressure']
    x4= insertValues['SkinThickness']
    x5= insertValues['Insulin']
    x6= insertValues['BMI']
    x7= insertValues['DiabetesPedigreeFunction']
    x8= insertValues['Age']
    input = np.array([[x1,x2,x3,x4,x5,x6,x7,x8]]).astype('float32')
    print(input)

    result = model.model_summary(input)
    return jsonify({'result':str(result)})




