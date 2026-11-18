// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00176(headers: HeaderMap) -> impl IntoResponse {
    let forwarded_ip = headers.get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = if forwarded_ip.len() <= 4096 { forwarded_ip.clone() } else { forwarded_ip.chars().take(4096).collect() };
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
