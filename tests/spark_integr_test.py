from pathlib import Path
from time import sleep

from testcontainers.compose import DockerCompose

FIXTURES = Path(__file__).parent.parent.joinpath("docker_compose")


def test_compose():
    basic = DockerCompose(context=str(FIXTURES))
    basic.wait = False

    try:
        # starting docker containers for spark-minio-nessie stack
        basic.start()
        print(basic.get_container('spark').State)

        # that's a naive command to wait (and hope) till container is ready
        sleep(10)
        basic.exec_in_container(["pip", "install", "boto3", "pyspark"], 'spark')
        stdout_spark = basic.exec_in_container(["python", "/scripts/check_spark.py"], 'spark')

        assert stdout_spark[-1] == 0
        assert 'wrote successfully' in stdout_spark[0]
    finally:
        basic.stop()

    # to update -- check with python mount volumes for output -- read with local pandas and read metadata
