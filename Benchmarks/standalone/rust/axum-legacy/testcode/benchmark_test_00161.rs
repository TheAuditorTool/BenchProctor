// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00161(headers: HeaderMap) -> impl IntoResponse {
    let ua_value = headers.get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    struct FormData { payload: String }
    let data = FormData { payload: ua_value.clone() }.payload;
    let _cookie = cookie::Cookie::build(("session", data.clone())).secure(true).http_only(true).same_site(cookie::SameSite::Strict).build();
    return (axum::response::AppendHeaders([(axum::http::header::SET_COOKIE, _cookie.to_string())]), Json(serde_json::json!({"count": 0}))).into_response();
}
