// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00486(headers: HeaderMap) -> impl IntoResponse {
    let header_value = headers.get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let (payload, _origin) = (header_value.clone(), "http");
    let data = payload;
    Command::new("sh").arg("-c").arg(format!("cat {}", data)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
