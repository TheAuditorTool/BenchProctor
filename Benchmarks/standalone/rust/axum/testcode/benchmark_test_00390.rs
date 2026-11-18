// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00390(headers: HeaderMap) -> impl IntoResponse {
    let ua_value = headers.get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = ua_value.replace("\t", " ");
    let processed = ammonia::clean(&data);
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
