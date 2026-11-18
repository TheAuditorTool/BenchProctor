// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;
use base64::Engine;
use base64::engine::general_purpose;

pub async fn benchmark_test_00527(headers: HeaderMap) -> impl IntoResponse {
    let cookie_value = headers.get("cookie").and_then(|v| v.to_str().ok()).and_then(|s| s.split(';').find(|c| c.trim_start().starts_with("session_token="))).map(|c| c.trim_start().trim_start_matches("session_token=").to_string()).unwrap_or_default();
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&cookie_value).unwrap_or_default()).to_string();
    crate::shared::set_cookie(&format!("session={}; Secure; HttpOnly; SameSite=Strict", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
