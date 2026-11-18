// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00122(headers: HeaderMap) -> impl IntoResponse {
    let referer_value = headers.get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = urlencoding::decode(&referer_value).unwrap_or_default().to_string();
    let processed = ammonia::clean(&data);
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
