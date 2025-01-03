#!/bin/sh

mkdir -p /app;
cd /scripts;
echo "installing boto3 and pyspark";
#pip install poetry=='1.8.1';
#export POETRY_VIRTUALENVS_CREATE=false;
#poetry install --no-root --no-interaction --without unit_tests,quality_checks,docs;
pip install boto3;
pip install pyspark;

echo "start check spark";

python check_spark.py;
