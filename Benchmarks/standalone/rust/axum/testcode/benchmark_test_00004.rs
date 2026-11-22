// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00004() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(env_value.clone());
    crate::shared::set_cookie(&format!("session={}; HttpOnly; SameSite=Strict", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
