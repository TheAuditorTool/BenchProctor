// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00054(headers: HeaderMap) -> impl IntoResponse {
    let auth_header = headers.get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = auth_header.to_string();
    let processed = html_escape::encode_text(&data).to_string();
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
