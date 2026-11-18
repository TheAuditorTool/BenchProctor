// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00487() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let data = match env_value.chars().next() { Some(_) => env_value.clone(), None => "default".to_string() };
    if !["ls", "cat", "date", "whoami"].contains(&data.as_str()) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let processed = data.clone();
    Command::new("sh").arg("-c").arg(format!("cat {}", processed)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
