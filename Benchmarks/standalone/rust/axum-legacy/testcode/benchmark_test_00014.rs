// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00014(headers: HeaderMap) -> impl IntoResponse {
    let auth_header = headers.get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match auth_header.chars().next() { Some(_) => auth_header.clone(), None => "default".to_string() };
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
