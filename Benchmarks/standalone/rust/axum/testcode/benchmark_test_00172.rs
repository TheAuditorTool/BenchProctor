// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00172(headers: HeaderMap) -> impl IntoResponse {
    let auth_header = headers.get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", auth_header).ok();
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
