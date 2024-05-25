#!/bin/bash
set -e

while ! clickhouse-client --host localhost --query "SELECT 1" ; do
  echo "Waiting for ClickHouse server..."
  sleep 1
done

echo "ClickHouse server started"

clickhouse-client --query="INSERT INTO default.logs FORMAT CSV" < /data/key_features.csv

echo "Data loaded"