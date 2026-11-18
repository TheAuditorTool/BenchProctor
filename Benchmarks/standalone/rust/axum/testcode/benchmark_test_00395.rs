// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00395(headers: HeaderMap) -> impl IntoResponse {
    let referer_value = headers.get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(referer_value.clone());
    axum::response::Redirect::to(data.as_str()).into_response()
}
