// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00273(headers: HeaderMap) -> impl IntoResponse {
    let host_value = headers.get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = host_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| host_value.clone());
    tokio::fs::write(format!("/var/app/data/{}", data), "data").await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
