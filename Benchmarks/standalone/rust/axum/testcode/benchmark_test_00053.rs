// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00053(headers: HeaderMap) -> impl IntoResponse {
    let ua_value = headers.get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let (payload, _origin) = (ua_value.clone(), "http");
    let data = payload;
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
