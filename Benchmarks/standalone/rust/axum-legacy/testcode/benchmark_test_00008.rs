// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00008(headers: HeaderMap) -> impl IntoResponse {
    let host_value = headers.get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(host_value.clone());
    let _cookie = cookie::Cookie::build(("session", data.clone())).secure(true).http_only(true).same_site(cookie::SameSite::Strict).build();
    return (axum::response::AppendHeaders([(axum::http::header::SET_COOKIE, _cookie.to_string())]), Json(serde_json::json!({"count": 0}))).into_response();
}
