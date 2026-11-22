// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00042(headers: HeaderMap) -> impl IntoResponse {
    let origin_value = headers.get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let captured = origin_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    axum::response::Redirect::to(data.as_str()).into_response()
}
