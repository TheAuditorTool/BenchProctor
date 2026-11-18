// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00282(headers: HeaderMap) -> impl IntoResponse {
    let header_value = headers.get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = header_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| header_value.clone());
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    crate::shared::store_session("data", &processed);
    Json(serde_json::json!({"count": 0})).into_response()
}
