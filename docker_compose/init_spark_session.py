import logging
import os

from pyspark.sql import SparkSession
from pyspark.conf import SparkConf


# init logic taken from
# https://medium.com/@wajahatullah.k/transforming-spark-dataframes-into-iceberg-tables-a-step-by-step-guide-6484e8b6b553

conf = (
    SparkConf()
        .setAppName('SparkIntegrTest')
        .set('spark.jars.packages',
             'org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.7.1,org.apache.iceberg:iceberg-aws-bundle:1.7.1,org.projectnessie.nessie-integrations:nessie-spark-extensions-3.5_2.12:0.95.0')
        .set('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions,org.projectnessie.spark.extensions.NessieSparkSessionExtensions')

        # nessie catalog params
        .set('spark.sql.catalog.nessie', 'org.apache.iceberg.spark.SparkCatalog')
        .set('spark.sql.catalog.nessie.catalog-impl', 'org.apache.iceberg.nessie.NessieCatalog')
        .set('spark.sql.catalog.nessie.uri', os.getenv('NESSIE_ENDPOINT'))
        # .set('spark.sql.catalog.nessie.s3.endpoint', os.getenv('MINIO_ENDPOINT'))
        .set('spark.sql.catalog.nessie.warehouse', 's3a://landing')

        # aws creds
        # .set("spark.sql.catalog.nessie.client.credentials-provider",
        #      "software.amazon.awssdk.auth.credentials.SystemPropertyCredentialsProvider")
        # .set("spark.sql.catalog.nessie.s3.access-key-id", os.getenv('MINIO_SERVER_ACCESS_KEY'))
        # .set("spark.sql.catalog.nessie.s3.secret-access-key", os.getenv('MINIO_SERVER_SECRET_KEY'))

        .set('spark.sql.catalog.nessie.ref', 'main')
        # .set('spark.sql.catalog.nessie.cache-enabled', 'false')
        # .set('spark.sql.catalog.nessie.io-impl', 'org.apache.iceberg.aws.s3.S3FileIO')
        .set("spark.sql.catalog.nessie.authentication.type", "NONE")

        # hadoop configs
        .set('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
        .set('spark.hadoop.fs.s3a.path.style.access', 'true')
        .set('spark.hadoop.fs.s3a.connection.ssl.enabled', 'false')
        .set('spark.hadoop.fs.s3a.endpoint', os.getenv('MINIO_ENDPOINT'))
        .set('spark.hadoop.fs.s3a.access.key', os.getenv('MINIO_SERVER_ACCESS_KEY'))
        .set('spark.hadoop.fs.s3a.secret.key', os.getenv('MINIO_SERVER_SECRET_KEY'))
        .set('spark.hadoop.fs.s3a.endpoint.region', os.getenv('AWS_REGION'))
        .set('aws.region', os.getenv('AWS_REGION'))
)
#
# .config("spark.sql.catalog.AwsDataCatalog.s3.access-key-id", "xxx")
# .config("spark.sql.catalog.AwsDataCatalog.s3.secret-access-key", "xxx")
# .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,org.slf4j:slf4j-simple:1.6.1,org.slf4j:slf4j-api:1.6.1,org.projectnessie.nessie-integrations:nessie-spark-extensions-3.5_2.12:0.91.2,org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.5.2,software.amazon.awssdk:bundle:2.17.257,software.amazon.awssdk:url-connection-client:2.17.257")
# .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions,org.projectnessie.spark.extensions.NessieSparkSessionExtensions")
# .config("spark.kryo.registrator", "org.apache.sedona.core.serde.SedonaKryoRegistrator")
# .config("spark.sql.catalog.nessie", "org.apache.iceberg.spark.SparkCatalog")
# .config("spark.sql.catalog.nessie.catalog-impl", "org.apache.iceberg.nessie.NessieCatalog")
# .config("spark.sql.catalog.nessie.io-impl", "org.apache.iceberg.aws.s3.S3FileIO")
# .config("spark.sql.catalog.nessie.warehouse", "s3a://xxx/nessie")
# .config("spark.sql.catalog.nessie.s3.endpoint", "https://xxx")
# .config("spark.sql.catalog.nessie.uri", "http://xxx")
# .config("spark.sql.catalog.nessie.ref", "main")
# .config("spark.sql.catalog.nessie.authentication.type", "NONE")
# .config"spark.sql.warehouse.dir", "s3a://xxx/nessie")
# .config("spark.sql.catalog.nessie.client.credentials-provider", "software.amazon.awssdk.auth.credentials.SystemPropertyCredentialsProvider")
# .config("spark.driver.extraJavaOptions", "-Daws.region=eu-central-1")
# .config("spark.executor.extraJavaOptions", "-Daws.region=eu-central-1")
# .config("spark.sql.catalog.nessie.s3.access-key-id", "xxx")
# .config("spark.sql.catalog.nessie.s3.secret-access-key", "xxx")

# Initializing spark session
def init_spark():
    # dbg
    logging.info(f"loaded aws creds {os.getenv('MINIO_SERVER_ACCESS_KEY'), os.getenv('MINIO_SERVER_SECRET_KEY')} ")
    # dbg

    logging.info('Initializing spark session')
    return SparkSession.builder.config(conf=conf).getOrCreate()

