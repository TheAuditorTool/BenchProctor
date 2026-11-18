// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00529(headers: HeaderMap) -> impl IntoResponse {
    let ua_value = headers.get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut data = String::new();
    for token in ua_value.split(',') { data = token.to_string(); }
    Command::new("bash").arg("-c").arg(format!("echo {}", data)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
