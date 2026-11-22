// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00004(headers: HeaderMap) -> impl IntoResponse {
    let auth_header = headers.get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", auth_header).ok();
    return (axum::response::AppendHeaders([(axum::http::header::SET_COOKIE, format!("session={}; Secure; HttpOnly; SameSite=Strict", urlencoding::encode(&data)))]), Json(serde_json::json!({"count": 0}))).into_response();
}
