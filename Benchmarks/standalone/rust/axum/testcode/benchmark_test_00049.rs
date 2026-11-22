// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00049(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    struct FormData { payload: String }
    let data = FormData { payload: raw_body.clone() }.payload;
    let _cookie = cookie::Cookie::build(("session", data.clone())).http_only(true).same_site(cookie::SameSite::Strict).build();
    return (axum::response::AppendHeaders([(axum::http::header::SET_COOKIE, _cookie.to_string())]), Json(serde_json::json!({"count": 0}))).into_response();
}
