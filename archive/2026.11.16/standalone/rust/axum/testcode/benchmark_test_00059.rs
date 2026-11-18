// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00059(headers: HeaderMap) -> impl IntoResponse {
    let ua_value = headers.get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(ua_value.clone());
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
