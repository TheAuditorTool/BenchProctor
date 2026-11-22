// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00231(headers: HeaderMap) -> impl IntoResponse {
    let host_value = headers.get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = if host_value.len() <= 4096 { host_value.clone() } else { host_value.chars().take(4096).collect() };
    axum::response::Redirect::to(data.as_str()).into_response()
}
