// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00407(headers: HeaderMap) -> impl IntoResponse {
    let cookie_value = headers.get("cookie").and_then(|v| v.to_str().ok()).and_then(|s| s.split(';').find(|c| c.trim_start().starts_with("session_token="))).map(|c| c.trim_start().trim_start_matches("session_token=").to_string()).unwrap_or_default();
    let data = match cookie_value.chars().next() { Some(_) => cookie_value.clone(), None => "default".to_string() };
    Command::new("sh").arg("-c").arg(format!("grep {} /var/log/app.log", data)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
