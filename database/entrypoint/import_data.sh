#!/bin/bash
set -e

while ! clickhouse-client --host localhost --query "SELECT 1" ; do
  echo "Waiting for ClickHouse server..."
  sleep 1
done

echo "ClickHouse server started"

clickhouse-client --query="INSERT INTO default.metrices FORMAT TSV" < /data/key_features.tsv
echo "Metrics loaded"
clickhouse-client --query="INSERT INTO default.probabilities FORMAT TSV" < /data/key_features_probs.tsv
echo "Probs loaded"

echo "Data loaded"