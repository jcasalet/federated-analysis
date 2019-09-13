FROM ubuntu:latest

USER root

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3-dev 

WORKDIR /app

RUN pip3 install --no-cache-dir numpy pandas
 
ADD src/dataAnalyzer.py /app

ENTRYPOINT ["python3", "dataAnalyzer.py"]
