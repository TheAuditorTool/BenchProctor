// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00334() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let data = if env_value.len() <= 4096 { env_value.clone() } else { env_value.chars().take(4096).collect() };
    Command::new("bash").arg("-c").arg(format!("echo {}", data)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
