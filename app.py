import sys
sys.path.append('.')

import os
import numpy as np
import base64
import io

from PIL import Image
from flask import Flask, request, jsonify
from facesdk import getMachineCode
from facesdk import setActivation
from facesdk import initSDK
from facesdk import faceDetection
from facesdk import templateExtraction
from facesdk import similarityCalculation
from facebox import FaceBox

maxFaceCount = 8

licensePath = "license.txt"
license = ""

# Get a specific environment variable by name
license = os.environ.get("LICENSE")

# Check if the variable exists
if license is not None:
    print("Value of LICENSE:")
else:
    license = ""
    try:
        with open(licensePath, 'r') as file:
            license = file.read().strip()
    except IOError as exc:
        print("failed to open license.txt: ", exc.errno)
    print("license: ", license)

machineCode = getMachineCode()
print("machineCode: ", machineCode.decode('utf-8'))


ret = setActivation(license.encode('utf-8'))
print("activation: ", ret)

ret = initSDK("data".encode('utf-8'))
print("init: ", ret)

app = Flask(__name__) 

@app.route('/compare_face', methods=['POST'])
def compare_face():
    file1 = request.files['file1']
    file2 = request.files['file2']

    try:
        image1 = Image.open(file1).convert('RGB')
    except:
        result = "Failed to open file1"
        response = jsonify({"resultCode": result})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response


    try:
        image2 = Image.open(file2).convert('RGB')
    except:
        result = "Failed to open file2"
        response = jsonify({"resultCode": result})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    image_np1 = np.asarray(image1)
    image_np2 = np.asarray(image2)

    faceBoxes1 = (FaceBox * maxFaceCount)()
    faceCount1 = faceDetection(image_np1, image_np1.shape[1], image_np1.shape[0], faceBoxes1, maxFaceCount)

    faceBoxes2 = (FaceBox * maxFaceCount)()
    faceCount2 = faceDetection(image_np2, image_np2.shape[1], image_np2.shape[0], faceBoxes2, maxFaceCount)

    faces1_result = []
    faces2_result = []
    for i in range(faceCount1):
        templateExtraction(image_np1, image_np1.shape[1], image_np1.shape[0], faceBoxes1[i])

        landmark_68 = []
        for j in range(68):
            landmark_68.append({"x": faceBoxes1[i].landmark_68[j * 2], "y": faceBoxes1[i].landmark_68[j * 2 + 1]})

        face = {"x1": faceBoxes1[i].x1, "y1": faceBoxes1[i].y1, "x2": faceBoxes1[i].x2, "y2": faceBoxes1[i].y2, 
                      "yaw": faceBoxes1[i].yaw, "roll": faceBoxes1[i].roll, "pitch": faceBoxes1[i].pitch,
                      "face_quality": faceBoxes1[i].face_quality, "face_luminance": faceBoxes1[i].face_luminance, "eye_dist": faceBoxes1[i].eye_dist,
                      "left_eye_closed": faceBoxes1[i].left_eye_closed, "right_eye_closed": faceBoxes1[i].right_eye_closed,
                      "face_occlusion": faceBoxes1[i].face_occlusion, "mouth_opened": faceBoxes1[i].mouth_opened,
                      "landmark_68": landmark_68}
        
        faces1_result.append(face)

    for i in range(faceCount2):
        templateExtraction(image_np2, image_np2.shape[1], image_np2.shape[0], faceBoxes2[i])

        landmark_68 = []
        for j in range(68):
            landmark_68.append({"x": faceBoxes2[i].landmark_68[j * 2], "y": faceBoxes2[i].landmark_68[j * 2 + 1]})


        face = {"x1": faceBoxes2[i].x1, "y1": faceBoxes2[i].y1, "x2": faceBoxes2[i].x2, "y2": faceBoxes2[i].y2, 
                      "yaw": faceBoxes2[i].yaw, "roll": faceBoxes2[i].roll, "pitch": faceBoxes2[i].pitch,
                      "face_quality": faceBoxes2[i].face_quality, "face_luminance": faceBoxes2[i].face_luminance, "eye_dist": faceBoxes2[i].eye_dist,
                      "left_eye_closed": faceBoxes2[i].left_eye_closed, "right_eye_closed": faceBoxes2[i].right_eye_closed,
                      "face_occlusion": faceBoxes2[i].face_occlusion, "mouth_opened": faceBoxes2[i].mouth_opened,
                      "landmark_68": landmark_68}
        
        faces2_result.append(face)

    
    if faceCount1 > 0 and faceCount2 > 0:
        results = []
        for i in range(faceCount1):
            for j in range(faceCount2): 
                similarity = similarityCalculation(faceBoxes1[i].templates, faceBoxes2[j].templates)
                match_result = {"face1": i, "face2": j, "similarity": similarity}
                results.append(match_result)

        response = jsonify({"resultCode": "Ok", "faces1": faces1_result, "faces2": faces2_result, "results": results})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    elif faceCount1 == 0:
        response = jsonify({"resultCode": "No face1", "faces1": faces1_result, "faces2": faces2_result})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    elif faceCount2 == 0:
        response = jsonify({"resultCode": "No face2", "faces1": faces1_result, "faces2": faces2_result})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

        
@app.route('/compare_face_base64', methods=['POST'])
def compare_face_base64():
    content = request.get_json()

    try:
        imageBase64_1 = content['base64_1']
        image_data1 = base64.b64decode(imageBase64_1)    
        image1 = Image.open(io.BytesIO(image_data1)).convert('RGB')
    except:
        result = "Failed to open file1"
        response = jsonify({"resultCode": result})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    
    try:
        imageBase64_2 = content['base64_2']
        image_data2 = base64.b64decode(imageBase64_2)
        image2 = Image.open(io.BytesIO(image_data2)).convert('RGB')
    except IOError as exc:
        result = "Failed to open file1"
        response = jsonify({"resultCode": result})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    image_np1 = np.asarray(image1)
    image_np2 = np.asarray(image2)

    faceBoxes1 = (FaceBox * maxFaceCount)()
    faceCount1 = faceDetection(image_np1, image_np1.shape[1], image_np1.shape[0], faceBoxes1, maxFaceCount)

    faceBoxes2 = (FaceBox * maxFaceCount)()
    faceCount2 = faceDetection(image_np2, image_np2.shape[1], image_np2.shape[0], faceBoxes2, maxFaceCount)

    faces1_result = []
    faces2_result = []
    for i in range(faceCount1):
        templateExtraction(image_np1, image_np1.shape[1], image_np1.shape[0], faceBoxes1[i])

        landmark_68 = []
        for j in range(68):
            landmark_68.append({"x": faceBoxes1[i].landmark_68[j * 2], "y": faceBoxes1[i].landmark_68[j * 2 + 1]})

        face = {"x1": faceBoxes1[i].x1, "y1": faceBoxes1[i].y1, "x2": faceBoxes1[i].x2, "y2": faceBoxes1[i].y2, 
                      "yaw": faceBoxes1[i].yaw, "roll": faceBoxes1[i].roll, "pitch": faceBoxes1[i].pitch,
                      "face_quality": faceBoxes1[i].face_quality, "face_luminance": faceBoxes1[i].face_luminance, "eye_dist": faceBoxes1[i].eye_dist,
                      "left_eye_closed": faceBoxes1[i].left_eye_closed, "right_eye_closed": faceBoxes1[i].right_eye_closed,
                      "face_occlusion": faceBoxes1[i].face_occlusion, "mouth_opened": faceBoxes1[i].mouth_opened,
                      "landmark_68": landmark_68}
        
        faces1_result.append(face)

    for i in range(faceCount2):
        templateExtraction(image_np2, image_np2.shape[1], image_np2.shape[0], faceBoxes2[i])

        landmark_68 = []
        for j in range(68):
            landmark_68.append({"x": faceBoxes2[i].landmark_68[j * 2], "y": faceBoxes2[i].landmark_68[j * 2 + 1]})


        face = {"x1": faceBoxes2[i].x1, "y1": faceBoxes2[i].y1, "x2": faceBoxes2[i].x2, "y2": faceBoxes2[i].y2, 
                      "yaw": faceBoxes2[i].yaw, "roll": faceBoxes2[i].roll, "pitch": faceBoxes2[i].pitch,
                      "face_quality": faceBoxes2[i].face_quality, "face_luminance": faceBoxes2[i].face_luminance, "eye_dist": faceBoxes2[i].eye_dist,
                      "left_eye_closed": faceBoxes2[i].left_eye_closed, "right_eye_closed": faceBoxes2[i].right_eye_closed,
                      "face_occlusion": faceBoxes2[i].face_occlusion, "mouth_opened": faceBoxes2[i].mouth_opened,
                      "landmark_68": landmark_68}
        
        faces2_result.append(face)

    
    if faceCount1 > 0 and faceCount2 > 0:
        results = []
        for i in range(faceCount1):
            for j in range(faceCount2): 
                similarity = similarityCalculation(faceBoxes1[i].templates, faceBoxes2[j].templates)
                match_result = {"face1": i, "face2": j, "similarity": similarity}
                results.append(match_result)

        response = jsonify({"resultCode": "Ok", "faces1": faces1_result, "faces2": faces2_result, "results": results})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    elif faceCount1 == 0:
        response = jsonify({"resultCode": "No face1", "faces1": faces1_result, "faces2": faces2_result})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    elif faceCount2 == 0:
        response = jsonify({"resultCode": "No face2", "faces1": faces1_result, "faces2": faces2_result})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
