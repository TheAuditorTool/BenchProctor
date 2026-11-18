// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00025() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(env_value.clone());
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = result.unwrap();
    let _ = value;
    Json(serde_json::json!({"count": 0})).into_response()
}
