#!/bin/sh

sleep 10;
/usr/bin/mc config host add myminio http://minio:9000 minioadmin minioadmin;
sleep 10;
/usr/bin/mc mb myminio/bronze;
/usr/bin/mc policy download myminio/bronze;
/usr/bin/mc mb myminio/landing;
/usr/bin/mc policy download myminio/landing;
/usr/bin/mc put /resources/test_csv.csv myminio/landing/resources/test_csv.csv;

exit 0;
