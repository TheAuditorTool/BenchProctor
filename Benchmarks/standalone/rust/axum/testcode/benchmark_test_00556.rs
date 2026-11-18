// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00556(headers: HeaderMap) -> impl IntoResponse {
    let header_value = headers.get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let captured = header_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    Command::new("echo").arg(&data).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
