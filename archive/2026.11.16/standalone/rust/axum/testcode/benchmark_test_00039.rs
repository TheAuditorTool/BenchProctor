// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00039(headers: HeaderMap) -> impl IntoResponse {
    let auth_header = headers.get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = if auth_header.len() <= 4096 { auth_header.clone() } else { auth_header.chars().take(4096).collect() };
    reqwest::get(&data).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
