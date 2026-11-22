// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;

pub async fn benchmark_test_00099(headers: HeaderMap) -> impl IntoResponse {
    let host_value = headers.get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = host_value.replace("\t", " ");
    (StatusCode::FOUND, [(axum::http::header::LOCATION, data.clone())]).into_response()
}
