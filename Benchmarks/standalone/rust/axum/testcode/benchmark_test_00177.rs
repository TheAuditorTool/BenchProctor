// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00177(headers: HeaderMap) -> impl IntoResponse {
    let cookie_value = headers.get("cookie").and_then(|v| v.to_str().ok()).and_then(|s| s.split(';').find(|c| c.trim_start().starts_with("session_token="))).map(|c| c.trim_start().trim_start_matches("session_token=").to_string()).unwrap_or_default();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", cookie_value).ok();
    Command::new("bash").arg("-c").arg(format!("echo {}", data)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
