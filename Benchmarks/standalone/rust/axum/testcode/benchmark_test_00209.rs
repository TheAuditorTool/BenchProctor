// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00209(headers: HeaderMap) -> impl IntoResponse {
    let ua_value = headers.get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = ua_value.to_string();
    return ([("content-type", "text/html")], format!("<div>{}</div>", html_escape::encode_text(&data))).into_response();
}
