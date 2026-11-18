// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00225() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", env_value).ok();
    Command::new("sh").arg("-c").arg(format!("grep {} /var/log/app.log", data)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
