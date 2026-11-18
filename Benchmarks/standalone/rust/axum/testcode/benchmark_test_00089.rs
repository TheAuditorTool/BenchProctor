// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00089(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let captured = raw_body.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let processed = shell_escape::escape(std::borrow::Cow::from(&data)).to_string();
    Command::new("sh").arg("-c").arg(format!("cat {}", processed)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
