// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00166(headers: HeaderMap) -> impl IntoResponse {
    let ua_value = headers.get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = if ua_value.len() <= 4096 { ua_value.clone() } else { ua_value.chars().take(4096).collect() };
    tokio::fs::remove_file(format!("/var/app/data/{}", data)).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
