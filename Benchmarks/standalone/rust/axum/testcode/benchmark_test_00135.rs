// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00135(headers: HeaderMap) -> impl IntoResponse {
    let cookie_value = headers.get("cookie").and_then(|v| v.to_str().ok()).and_then(|s| s.split(';').find(|c| c.trim_start().starts_with("session_token="))).map(|c| c.trim_start().trim_start_matches("session_token=").to_string()).unwrap_or_default();
    let captured = cookie_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    use sha2::Digest;
    let _ = sha2::Sha256::new().chain_update(data.as_bytes()).finalize();
    Json(serde_json::json!({"count": 0})).into_response()
}
