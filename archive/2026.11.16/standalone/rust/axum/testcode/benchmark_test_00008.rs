// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00008(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = if raw_body.len() <= 4096 { raw_body.clone() } else { raw_body.chars().take(4096).collect() };
    Command::new("sh").arg("-c").arg(format!("grep {} /var/log/app.log", data)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
