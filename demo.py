import gradio as gr
import requests
import datadog_api_client
import json
import io
import base64

from PIL import Image

def face_crop(image, face_rect):
    x1 = face_rect.get('x1')
    y1 = face_rect.get('y1')
    x2 = face_rect.get('x2')
    y2 = face_rect.get('y2')
    width = x2 - x1 + 1
    height = y2 - y1 + 1


    if x1 < 0:
        x1 = 0
    if y1 < 0:
        y1 = 0
    if x2 >= image.width:
        x2 = image.width - 1
    if y2 >= image.height:
        y2 = image.height - 1

    face_image = image.crop((x1, y1, x2, y2))
    face_image_ratio = face_image.width / float(face_image.height)
    resized_w = int(face_image_ratio * 150)
    resized_h = 150

    face_image = face_image.resize((int(resized_w), int(resized_h)))
    return face_image

def pil_image_to_base64(image, format="PNG"):
    """
    Converts a PIL.Image object to a Base64-encoded string.
    :param image: PIL.Image object
    :param format: Format to save the image, e.g., "PNG", "JPEG"
    :return: Base64-encoded string
    """
    # Save the image to a BytesIO buffer
    buffer = io.BytesIO()
    image.save(buffer, format=format)
    buffer.seek(0)  # Rewind the buffer

    # Convert the buffer's contents to a Base64 string
    base64_string = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return base64_string
    
def compare_face(frame1, frame2):
    url = "http://127.0.0.1:8080/compare_face"
    files = {'file1': open(frame1, 'rb'), 'file2': open(frame2, 'rb')}

    file1 = None
    file2 = None
    try:
        file1 = open(frame1, 'rb')
    except:
        return "Failed to open image1"

    try:
        file2 = open(frame2, 'rb')
    except:
        return "Failed to open image2"
    
    url = "http://127.0.0.1:8080/compare_face"
    files = {'file1': file1, 'file2': file2}
    result = requests.post(url=url, files=files)

    if result.ok:
        json_result = result.json()
       
        if json_result.get("resultCode") != "Ok":
            return json_result.get("resultCode")
        
        try:
            image1 = Image.open(frame1)
            image2 = Image.open(frame2)

            html = ""
            faces1 = json_result.get("faces1", {})           
            faces2 = json_result.get("faces2", {})
            results = json_result.get("results", {})
    
            for result in results:
                similarity = result.get('similarity')
                face1_idx = result.get('face1')
                face2_idx = result.get('face2')
    
                face_image1 = face_crop(image1, faces1[face1_idx])
                face_value1 = ('<img src="data:image/png;base64,{base64_image}" style="width: 100px; height: auto; object-fit: contain;"/>').format(base64_image=pil_image_to_base64(face_image1, format="PNG"))
    
                face_image2 = face_crop(image2, faces2[face2_idx])
                face_value2 = ('<img src="data:image/png;base64,{base64_image}" style="width: 100px; height: auto; object-fit: contain;"/>').format(base64_image=pil_image_to_base64(face_image2, format="PNG"))
    
                match_icon = '<svg fill="red" width="19" height="32" viewBox="0 0 19 32"><path d="M0 13.92V10.2H19V13.92H0ZM0 21.64V17.92H19V21.64H0Z"></path><path d="M14.08 0H18.08L5.08 32H1.08L14.08 0Z"></path></svg>'
                if similarity > 0.67:
                    match_icon = '<svg fill="green" width="19" height="32" viewBox="0 0 19 32"><path d="M0 13.9202V10.2002H19V13.9202H0ZM0 21.6402V17.9202H19V21.6402H0Z"></path></svg>'
    
                item_value = ('<div style="align-items: center; gap: 10px; display: flex; flex-direction: column;">'
                                '<div style="display: flex; align-items: center; gap: 20px;">'
                                '{face_value1}'
                                '{match_icon}'
                                '{face_value2}'
                                '</div>'
                                '<div style="text-align: center; margin-top: 10px;">'
                                'Similarity: {similarity}'
                                '</div>'
                                '</div>'
                ).format(face_value1=face_value1, face_value2=face_value2, match_icon=match_icon, similarity=f"{similarity:.2f}")

                html += item_value
                html += '<hr style="border: 1px solid #C0C0C0; margin: 10px 0;"/>'
    
            return html
        except:
            return "Processing failed"
    else:
        return result.text

with gr.Blocks() as demo:
    gr.Markdown(
        """
    # KBY-AI
    We offer SDKs for Face Recognition, Face Liveness Detection(Face Anti-Spoofing), and ID Card Recognition.<br/>
    Besides that, we can provide several AI models and development services in machine learning.

    ## Simple Installation & Simple API
    ```
    sudo docker pull kbyai/face-recognition:latest
    sudo docker run -e LICENSE="xxxxx" -p 8081:8080 -p 9001:9000 kbyai/face-recognition:latest
    ```      
    ## KYC Verification Demo
    https://github.com/kby-ai/KYC-Verification    
    """
    )
    with gr.TabItem("Face Recognition"):
        with gr.Row():
            with gr.Column(scale=7):
                with gr.Row():
                    with gr.Column():
                        image_input1 = gr.Image(type='filepath')
                        gr.Examples(['face_examples/1.jpg', 'face_examples/3.jpg', 'face_examples/7.jpg', 'face_examples/9.jpg'], 
                                inputs=image_input1)
                    with gr.Column():
                        image_input2 = gr.Image(type='filepath')
                        gr.Examples(['face_examples/2.jpg', 'face_examples/4.jpg', 'face_examples/8.jpg', 'face_examples/10.jpg'], 
                                inputs=image_input2)
                face_recog_button = gr.Button("Compare Face", variant="primary", size="lg")
            with gr.Column(scale=3):
                recog_html_output = gr.HTML()

        face_recog_button.click(compare_face, inputs=[image_input1, image_input2], outputs=recog_html_output)

demo.launch(server_name="0.0.0.0", server_port=9000)