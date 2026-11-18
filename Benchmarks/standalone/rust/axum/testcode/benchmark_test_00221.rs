// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00221(headers: HeaderMap) -> impl IntoResponse {
    let host_value = headers.get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut data = String::new();
    for token in host_value.split(',') { data = token.to_string(); }
    reqwest::get(&data).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
