// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00586(headers: HeaderMap) -> impl IntoResponse {
    let header_value = headers.get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = header_value.replace("\t", " ");
    if !["ls", "cat", "date", "whoami"].contains(&data.as_str()) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let processed = data.clone();
    Command::new("sh").arg("-c").arg(format!("cat {}", processed)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
