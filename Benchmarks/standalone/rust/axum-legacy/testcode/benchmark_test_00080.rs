// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;

pub async fn benchmark_test_00080(headers: HeaderMap) -> impl IntoResponse {
    let origin_value = headers.get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let captured = origin_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    (StatusCode::FOUND, [(axum::http::header::LOCATION, data.clone())]).into_response()
}
