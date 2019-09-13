FROM ubuntu:latest

USER root

RUN apt-get update && apt-get install -y \
    python3.5 \
    python3-pip \
    python3-dev 

#WORKDIR /app

RUN pip3 install --no-cache-dir numpy pandas

#ADD app/dataAnalyzer.py /app/dataAnalyzer.py
#ADD app/customDataAnalyzer.py /app/customDataAnalyzer.py

#ENV PYTHONIOENCODING=UTF-8

#ENTRYPOINT ["python3", "/app/dataAnalyzer.py"]
