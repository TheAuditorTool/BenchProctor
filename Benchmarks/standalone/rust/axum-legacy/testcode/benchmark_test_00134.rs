// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00134() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let _prefix: String = env_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => env_value.to_lowercase(),
        "f" => env_value.to_uppercase(),
        _ => env_value.trim().to_string(),
    };
    if let Ok(mut _app_context) = crate::shared::APP_CONTEXT.write() {
        _app_context.insert("partner_tier".to_string(), data.clone());
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
