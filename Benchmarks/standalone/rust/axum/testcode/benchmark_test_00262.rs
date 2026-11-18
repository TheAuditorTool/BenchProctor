// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00262(headers: HeaderMap) -> impl IntoResponse {
    let origin_value = headers.get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut pending: std::collections::VecDeque<String> = origin_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    tokio::fs::remove_file(format!("/var/app/data/{}", processed)).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
