-- Для хранения логов телеметрии
DROP TABLE IF EXISTS default.logs;

CREATE TABLE default.logs
(
    account_id String,
    name String,
    point DateTime,
    call_count Float64,
    total_call_time Float64,
    total_exclusive_time Float64,
    min_call_time Float64,
    max_call_time Float64,
    sum_of_squares Float64,
    instances Float64,
    language String,
    app_name String,
    app_id String,
    scope String,
    host String,
    display_host String,
    pid String,
    agent_version String,
    labels String
)
ENGINE = MergeTree()
ORDER BY (account_id, app_id, point);

-- Для хранения предрассчитанных метрик для модели
DROP TABLE IF EXISTS default.metrices;

CREATE TABLE default.metrices
(
    point DateTime,
    web_response Float64,
    throughput Float64,
    apdex Float64,
    error Float64
)
ENGINE = MergeTree()
ORDER BY (point);   

-- Для хранения скоров модели
DROP TABLE IF EXISTS default.probabilities;

CREATE TABLE default.probabilities
(
    point DateTime,
    web_response_proba Float64,
    throughput_proba Float64,
    apdex_proba Float64,
    error_proba Float64
)
ENGINE = MergeTree()
ORDER BY (point);