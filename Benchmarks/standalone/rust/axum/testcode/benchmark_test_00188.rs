// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00188(headers: HeaderMap) -> impl IntoResponse {
    let ua_value = headers.get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = ua_value.to_string();
    if !["ls", "cat", "date", "whoami"].contains(&data.as_str()) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let processed = data.clone();
    Command::new("bash").arg("-c").arg(format!("echo {}", processed)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
