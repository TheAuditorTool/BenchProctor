// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00130(headers: HeaderMap) -> impl IntoResponse {
    let forwarded_ip = headers.get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", forwarded_ip).ok();
    let Some(at) = data.find('@') else { return (StatusCode::BAD_REQUEST, "").into_response(); };
    let mail_domain = &data[at + 1..];
    let _ = mail_domain;
    Json(serde_json::json!({"count": 0})).into_response()
}
