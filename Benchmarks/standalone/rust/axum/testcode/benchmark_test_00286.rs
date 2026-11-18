// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00286(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = raw_body.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    let processed = shell_escape::escape(std::borrow::Cow::from(&data)).to_string();
    Command::new("sh").arg("-c").arg(format!("grep {} /var/log/app.log", processed)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
