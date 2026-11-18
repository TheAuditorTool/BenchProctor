// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00074(headers: HeaderMap) -> impl IntoResponse {
    let forwarded_ip = headers.get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(forwarded_ip.clone());
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
