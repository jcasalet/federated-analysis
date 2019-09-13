#!/bin/bash

APP_PATH=/Users/jcasaletto/PycharmProjects/BIOBANK/federated_data_analysis/app
CONF_PATH=/Users/jcasaletto/PycharmProjects/BIOBANK/federated_data_analysis/config
DATA_PATH=/Users/jcasaletto/PycharmProjects/BIOBANK/federated_data_analysis/data

DOCKER_IMAGE_NAME=my_fda_image

docker run --rm -e PYTHONIOENCODING=UTF-8 -w /app --user=`id -u`:`id -g` -v ${APP_PATH}:/app:ro -v ${CONF_PATH}:/config -v "${DATA_PATH}":/data ${DOCKER_IMAGE_NAME} /usr/bin/python3 /app/dataAnalyzer.py /config/conf.json

