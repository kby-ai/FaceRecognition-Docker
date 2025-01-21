FROM openvino/ubuntu20_runtime:2022.3.0
USER root

RUN apt-get update -y
RUN apt-get install -y libcurl4-openssl-dev libssl-dev libgomp1 libpugixml-dev

RUN mkdir -p /root/kby-ai-face
WORKDIR /root/kby-ai-face
COPY ./libkbyai_facesdk2.so .
COPY ./libimutils.so /usr/lib/libimutils.so
COPY ./facesdk.py .
COPY ./facebox.py .
COPY ./app.py .
COPY ./demo.py .
COPY ./run.sh .
COPY ./face_examples ./face_examples
COPY ./requirements.txt .
COPY ./data ./data
RUN chmod a+x run.sh
RUN pip3 install -r requirements.txt
CMD ["./run.sh"]
EXPOSE 8080 9000
