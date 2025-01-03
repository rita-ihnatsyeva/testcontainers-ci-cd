#!/bin/sh

mkdir -p /app;
cd /scripts;
echo "installing boto3 and pyspark";
pip install boto3;
pip install pyspark;

echo "start check spark";

python check_spark.py;
