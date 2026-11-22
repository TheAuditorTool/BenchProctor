// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00097(headers: HeaderMap) -> impl IntoResponse {
    let ua_value = headers.get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let captured = ua_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let at = data.find('@').unwrap();
    let mail_domain = &data[at + 1..];
    let _ = mail_domain;
    Json(serde_json::json!({"count": 0})).into_response()
}
