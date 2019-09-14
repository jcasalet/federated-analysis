#!/bin/bash

FDA_PATH=/Users/jcasaletto/PycharmProjects/BIOBANK/federated_data_analysis

APP_PATH=${FDA_PATH}/app
CONF_PATH=${FDA_PATH}/config
DATA_PATH=${FDA_PATH}/data

DOCKER_IMAGE_NAME=my_fda_image

docker run --rm -e PYTHONIOENCODING=UTF-8 -w /app --user=`id -u`:`id -g` -v ${APP_PATH}:/app:ro -v ${CONF_PATH}:/config -v "${DATA_PATH}":/data ${DOCKER_IMAGE_NAME} /usr/bin/python3 /app/dataAnalyzer.py /config/conf.json

