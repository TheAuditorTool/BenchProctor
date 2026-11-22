// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00155(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    tokio::process::Command::new("grep").arg("-e").arg(&raw_body).arg("/var/log/app.log").output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
