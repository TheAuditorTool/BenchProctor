// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00411(headers: HeaderMap) -> impl IntoResponse {
    let host_value = headers.get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    struct FormData { payload: String }
    let data = FormData { payload: host_value.clone() }.payload;
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", data)).await;
    Json(serde_json::json!({"count": 0})).into_response()
}
