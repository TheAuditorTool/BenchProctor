// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00291(headers: HeaderMap) -> impl IntoResponse {
    let auth_header = headers.get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = if auth_header.len() <= 4096 { auth_header.clone() } else { auth_header.chars().take(4096).collect() };
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = result.unwrap();
    let _ = value;
    Json(serde_json::json!({"count": 0})).into_response()
}
