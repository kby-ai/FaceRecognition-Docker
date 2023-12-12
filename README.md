<p align="center">
  <a href="https://play.google.com/store/apps/dev?id=7086930298279250852" target="_blank">
    <img alt="" src="https://github-production-user-asset-6210df.s3.amazonaws.com/125717930/246971879-8ce757c3-90dc-438d-807f-3f3d29ddc064.png" width=500/>
  </a>  
</p>

👏 Product List

https://github.com/kby-ai/Product

👏  We have published the Face Liveness Detection, Face Recognition SDK and ID Card Recognition SDK for the server.

  - [FaceLivenessDetection-Docker](https://github.com/kby-ai/FaceLivenessDetection-Docker)

  - [FaceRecognition-Docker](https://github.com/kby-ai/FaceRecognition-Docker)

  - [IDCardRecognition-Docker](https://github.com/kby-ai/IDCardRecognition-Docker)

# FaceRecognition-Docker
## Overview
This project demonstrates an advanced face recognition technology implemented via a Dockerized Flask API.

It includes features that allow for testing face recognition between two images using both image files and base64-encoded images.

> The demo is integrated with KBY-AI's Face Recognition Server SDK.

> We can customize the SDK to align with your specific requirements.

  | Face Liveness Detection      | Face Recognition |
  |------------------|------------------|
  | Face Detection        | Face Detection    |
  | Face Liveness Detection        | Face Recognition    |
  | Pose Estimation        | Pose Estimation    |
  | 68 points Face Landmark Detection        | 68 points Face Landmark Detection    |
  | Face Quality Calculation        | Face Occlusion Detection        |
  | Face Occlusion Detection        | Face Occlusion Detection        |
  | Eye Closure Detection        | Eye Closure Detection       |
  | Mouth Opening Check        | Mouth Opening Check        |

> For other solutions, please explore the following:
>
> [Face Liveness Detection - Android(Basic SDK)](https://github.com/kby-ai/FaceLivenessDetection-Android)
>
> [Face Liveness Detection - iOS(Basic SDK)](https://github.com/kby-ai/FaceLivenessDetection-iOS)
>
> [Face Recognition - Android(Standard SDK)](https://github.com/kby-ai/FaceRecognition-Android)
>
> [Face Recognition - iOS(Standard SDK)](https://github.com/kby-ai/FaceRecognition-iOS)
>
> [Face Recognition - Flutter(Standard SDK)](https://github.com/kby-ai/FaceRecognition-Flutter)
>
> [Face Recognition - React-Native(Standard SDK)](https://github.com/kby-ai/FaceRecognition-React-Native)
>
> [Face Attribute - Android(Premium SDK)](https://github.com/kby-ai/FaceAttribute-Android)
>
> [Face Attribute - iOS(Premium SDK)](https://github.com/kby-ai/FaceAttribute-iOS)

## Try the API
### Online Demo
  You can test the SDK using images from the following URL:
  https://web.kby-ai.com
  
  ![image](https://github.com/kby-ai/FaceRecognition-Docker/assets/125717930/a7aa607c-8c40-4ef0-9592-7332c97457ca)
  
### Postman
  To test the API, you can use Postman. Here are the endpoints for testing:
  - Test with an image file: Send a POST request to http://18.221.33.238:8081/compare_face
  - Test with a base64-encoded image: Send a POST request to http://18.221.33.238:8081/compare_face_base64

    You can download the Postman collection to easily access and use these endpoints. [click here](https://github.com/kby-ai/FaceRecognition-Docker/tree/main/postman/kby-ai-face.postman_collection.json)
    
    ![image](https://github.com/kby-ai/FaceRecognition-Docker/assets/125717930/dce48454-6d41-46f0-9623-b26bec103616)


## SDK License

This project uses KBY-AI's Face Recognition Server SDK, which requires a license per machine.

- The code below shows how to use the license: https://github.com/kby-ai/FaceRecognition-Docker/blob/5c6bdaff0e8154d6c6472ac9faf9158c6a6e7b47/app.py#L26-L36

- In order to request the license, please provide us with the machine code obtained from the "getMachineCode" function.

  Please contact us:
  ```
  Email: contact@kby-ai.com

  Telegram: @kbyai

  WhatsApp: +19092802609

  Skype: live:.cid.66e2522354b1049b

  Facebook: https://www.facebook.com/KBYAI
  
## How to run

### 1. System Requirements
  - CPU: 2 cores or more (Recommended: 2 cores)
  - RAM: 4 GB or more (Recommended: 8 GB)
  - HDD: 4 GB or more (Recommended: 8 GB)
  - OS: Ubuntu 20.04 or later
  - Dependency: OpenVINO™ Runtime (Version: 2022.3)

### 2. Setup and Test
  - Clone the project:
    ```
    git clone https://github.com/kby-ai/FaceRecognition-Docker.git
    ```
  - Download the model from Google Drive: [click here](https://drive.google.com/file/d/19vA7ZOlo19BcW8v4iCoCGahUEbgKCo48/view?usp=sharing)
    ```
    cd FaceRecognition-Docker
    
    wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=19vA7ZOlo19BcW8v4iCoCGahUEbgKCo48' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=19vA7ZOlo19BcW8v4iCoCGahUEbgKCo48" -O data.zip && rm -rf /tmp/cookies.txt
    
    unzip data.zip
    ```
  - Build the Docker image:
    ```
    sudo docker build --pull --rm -f Dockerfile -t kby-ai-face:latest .
    ```
  - Run the Docker container:
    ```
    sudo docker run -v ./license.txt:/home/openvino/kby-ai-face/license.txt -p 8081:8080 kby-ai-face
    ```
  - Send us the machine code and then we will give you a license key.
  
    After that, update the license.txt file by overwriting the license key that you received. Then, run the Docker container again.
    
    ![image](https://github.com/kby-ai/FaceRecognition-Docker/assets/125717930/d7e84054-e4da-42c4-a88f-e74d50387d92)
    
    ![image](https://github.com/kby-ai/FaceRecognition-Docker/assets/125717930/7988b167-17dd-4501-8168-871954a1c8ec)

  - To test the API, you can use Postman. Here are the endpoints for testing:

    Test with an image file: Send a POST request to http://{xx.xx.xx.xx}:8081/compare_face
    
    Test with a base64-encoded image: Send a POST request to http://{xx.xx.xx.xx}:8081/compare_face_base64
    
    You can download the Postman collection to easily access and use these endpoints. [click here](https://github.com/kby-ai/FaceRecognition-Docker/tree/main/postman/kby-ai-face.postman_collection.json)

### 3. Execute the Gradio demo
  - Setup Gradio
    Ensure that you have the necessary dependencies installed. 
    
    Gradio requires Python 3.6 or above. 
    
    You can install Gradio using pip by running the following command:
    ```
    pip install gradio
    ```
  - Run the demo
    Run it using the following command:
    ```
    cd gradio
    python demo.py
    ```
  - You can test within the following URL:    
    http://127.0.0.1:9000

## About SDK

### 1. Initializing the SDK

- Step One

  First, obtain the machine code for activation and request a license based on the machine code.
  ```
  machineCode = getMachineCode()
  print("machineCode: ", machineCode.decode('utf-8'))
  ```
  
- Step Two

  Next, activate the SDK using the received license.
  ```
  setActivation(license.encode('utf-8'))
  ```  
  If activation is successful, the return value will be SDK_SUCCESS. Otherwise, an error value will be returned.

- Step Three

  After activation, call the initialization function of the SDK.
  ```
  initSDK("data".encode('utf-8'))
  ```
  The first parameter is the path to the model.

  If initialization is successful, the return value will be SDK_SUCCESS. Otherwise, an error value will be returned.

### 2. Enum and Structure
  - SDK_ERROR
  
    This enumeration represents the return value of the 'initSDK' and 'setActivation' functions.

    | Feature| Value | Name |
    |------------------|------------------|------------------|
    | Successful activation or initialization        | 0    | SDK_SUCCESS |
    | License key error        | -1    | SDK_LICENSE_KEY_ERROR |
    | AppID error (Not used in Server SDK)       | -2    | SDK_LICENSE_APPID_ERROR |
    | License expiration        | -3    | SDK_LICENSE_EXPIRED |
    | Not activated      | -4    | SDK_NO_ACTIVATED |
    | Failed to initialize SDK       | -5    | SDK_INIT_ERROR |

- FaceBox
  
    This structure represents the output of the face detection function.

    | Feature| Type | Name |
    |------------------|------------------|------------------|
    | Face rectangle        | int    | x1, y1, x2, y2 |
    | Face angles (-45 ~ 45)        | float    | yaw, roll, pitch |
    | Face quality (0 ~ 1)        | float    | face_quality |
    | Face luminance (0 ~ 255)       | float    | face_luminance |
    | Eye distance (pixels)       | float    | eye_dist |
    | Eye closure (0 ~ 1)       | float    | left_eye_closed, right_eye_closed |
    | Face occlusion (0 ~ 1)       | float    | face_occlusion |
    | Mouth opening (0 ~ 1)       | float    | mouth_opened |
    | 68 points facial landmark        | float [68 * 2]    | landmarks_68 |
    | Face templates        | unsigned char [2048]    | templates |
  
    > 68 points facial landmark
    
    <img src="https://user-images.githubusercontent.com/125717930/235560305-ee1b6a39-5dab-4832-a214-732c379cabfd.png" width=500/>

### 3. APIs
  - Face Detection
  
    The Face SDK provides a single API for detecting faces, determining face orientation (yaw, roll, pitch), assessing face quality, detecting facial occlusion, eye closure, mouth opening, and identifying facial landmarks.
    
    The function can be used as follows:

    ```
    faceBoxes = (FaceBox * maxFaceCount)()
    faceCount = faceDetection(image_np, image_np.shape[1], image_np.shape[0], faceBoxes, maxFaceCount)
    ```
    
    This function requires 5 parameters.
    * The first parameter: the byte array of the RGB image buffer.
    * The second parameter: the width of the image.
    * The third parameter: the height of the image.
    * The fourth parameter: the 'FaceBox' array allocated with 'maxFaceCount' for storing the detected faces.
    * The fifth parameter: the count allocated for the maximum 'FaceBox' objects.

    The function returns the count of the detected face.

  - Create Template

    The SDK provides a function that enables the generation of templates from RGB data. These templates can be used for face verification between two faces.

    The function can be used as follows:

    ```    
    templateExtraction(image_np1, image_np1.shape[1], image_np1.shape[0], faceBoxes1[0])
    ```

    This function requires 4 parameters.
    * The first parameter: the byte array of the RGB image buffer.
    * The second parameter: the width of the image.
    * The third parameter: the height of the image.
    * The fourth parameter: the 'FaceBox' object obtained from the 'faceDetection' function.

    If the template extraction is successful, the function will return 0. Otherwise, it will return -1.
    
  - Calculation similiarity

    The 'similarityCalculation' function takes a byte array of two templates as a parameter. 

    ```
    similarity = similarityCalculation(faceBoxes1[0].templates, faceBoxes2[0].templates)
    ```

    It returns the similarity value between the two templates, which can be used to determine the level of likeness between the two individuals.

### 4. Thresholds
  The default thresholds are as the following below:
  https://github.com/kby-ai/FaceRecognition-Docker/blob/75800590cd9f2a3b778ec176bf465d1a731278fa/app.py#L18-L20
