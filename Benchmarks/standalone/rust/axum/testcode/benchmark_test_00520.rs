// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00520(headers: HeaderMap) -> impl IntoResponse {
    let cookie_value = headers.get("cookie").and_then(|v| v.to_str().ok()).and_then(|s| s.split(';').find(|c| c.trim_start().starts_with("session_token="))).map(|c| c.trim_start().trim_start_matches("session_token=").to_string()).unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(cookie_value.clone());
    let processed = ammonia::clean(&data);
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
