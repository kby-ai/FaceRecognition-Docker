FROM openvino/ubuntu20_runtime:2022.3.0
    
RUN mkdir -p /home/openvino/kby-ai-face
WORKDIR /home/openvino/kby-ai-face
COPY ./libfacesdk2.so .
COPY ./facesdk.py .
COPY ./facebox.py .
COPY ./app.py .
COPY ./requirements.txt .
COPY ./data ./data
RUN pip3 install -r requirements.txt
CMD [ "python3", "app.py"]
EXPOSE 8080