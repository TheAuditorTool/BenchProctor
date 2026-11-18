// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00074(headers: HeaderMap) -> impl IntoResponse {
    let origin_value = headers.get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = origin_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| origin_value.clone());
    axum::response::Redirect::to(data.as_str()).into_response()
}
