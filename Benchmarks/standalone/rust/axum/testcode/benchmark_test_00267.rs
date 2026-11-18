// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00267(headers: HeaderMap) -> impl IntoResponse {
    let referer_value = headers.get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let (payload, _origin) = (referer_value.clone(), "http");
    let data = payload;
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
