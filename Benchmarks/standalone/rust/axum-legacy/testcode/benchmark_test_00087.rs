// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00087(headers: HeaderMap) -> impl IntoResponse {
    let cookie_value = headers.get("cookie").and_then(|v| v.to_str().ok()).and_then(|s| s.split(';').find(|c| c.trim_start().starts_with("session_token="))).map(|c| c.trim_start().trim_start_matches("session_token=").to_string()).unwrap_or_default();
    let data = urlencoding::decode(&cookie_value).unwrap_or_default().to_string();
    if !["ls", "cat", "date", "whoami"].contains(&data.as_str()) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let processed = data.clone();
    let _cmdline = std::ffi::CString::new(format!("grep {} /var/log/app.log", processed)).unwrap_or_default();
    unsafe { libc::system(_cmdline.as_ptr()) };
    Json(serde_json::json!({"count": 0})).into_response()
}
