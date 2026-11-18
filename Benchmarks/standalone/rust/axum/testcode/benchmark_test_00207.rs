// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00207(headers: HeaderMap) -> impl IntoResponse {
    let referer_value = headers.get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match referer_value.chars().next() { Some(_) => referer_value.clone(), None => "default".to_string() };
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
