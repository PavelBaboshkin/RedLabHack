DROP TABLE IF EXISTS default.logs;

CREATE TABLE default.logs
(
    point DateTime,
    web_response Float64,
    throughput Float64,
    apdex Float64,
    error Float64
)
ENGINE = MergeTree()
ORDER BY (point);   