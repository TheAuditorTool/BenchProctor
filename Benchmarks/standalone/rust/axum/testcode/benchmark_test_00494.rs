// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00494() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    tokio::fs::remove_file(format!("/var/app/data/{}", env_value)).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
