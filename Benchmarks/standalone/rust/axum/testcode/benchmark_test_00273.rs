// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00273() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let (payload, _origin) = (env_value.clone(), "http");
    let data = payload;
    Command::new("sh").arg("-c").arg(format!("cat {}", data)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
