import os
import logging
import boto3

from pyspark.sql.functions import *
from pyspark.sql.types import *

from init_spark_session import init_spark



logging.basicConfig(level=logging.INFO)

s3_resource = boto3.resource('s3',
    endpoint_url=os.getenv('MINIO_ENDPOINT'),
    aws_access_key_id=os.getenv('MINIO_SERVER_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('MINIO_SERVER_SECRET_KEY')
)

spark = init_spark()

# read csv from minio bucket
df = spark.read.options(delimiter=";", header=True).csv('s3a://landing/resources/test_csv.csv')

logging.info(df.show())

spark.sql("use nessie")

print(spark.sql("show tables").show())

print('writing to icebrg minio nessie')

df.write.format("iceberg").mode("overwrite").option("path","s3a://landing/csv_to_iceberg").saveAsTable("nessie.csv_to_iceberg")


# show table if save in iceberg
spark.sql("""select * from nessie.csv_to_iceberg""").show()

print('wrote successfully')

