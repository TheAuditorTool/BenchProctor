// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00194(headers: HeaderMap) -> impl IntoResponse {
    let header_value = headers.get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let result: Option<String> = std::env::var(header_value.as_str()).ok();
    let value = result.unwrap();
    let _ = value;
    Json(serde_json::json!({"count": 0})).into_response()
}
