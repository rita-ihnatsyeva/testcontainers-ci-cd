
# An example of integrational test for Spark-Minio-Nessie stack

For the local run:
* create and activate vert env with python version 3.12 (recommended)
  ```
  # create
  python3 -m venv <your ven env name>
  
  # activate (for linux users) 
  source <your ven env name>/bin/activate
  
  ```
* install docker if not present (https://docs.docker.com/engine/install/)
* istall dependencies from the requiremnts.txt
  ```
  pip install -r < path to requirements.txt>

  ```
* run pytest locally
  ```
  pytest ./tests/spark_integr_test.py
  ```

  # Detailed description of the approach can be found in the [Article](https://medium.com/@bggghffff116/spark-integration-tests-with-testcontcontainers-7b925a8175f3)



