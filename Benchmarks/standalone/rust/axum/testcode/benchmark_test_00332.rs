// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00332() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let data = match env_value.chars().next() { Some(_) => env_value.clone(), None => "default".to_string() };
    crate::shared::ldap_search(&format!("uid={}", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
