// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;

pub async fn benchmark_test_00204(headers: HeaderMap) -> impl IntoResponse {
    let referer_value = headers.get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = referer_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| referer_value.clone());
    (StatusCode::FOUND, [(axum::http::header::LOCATION, data.clone())]).into_response()
}
