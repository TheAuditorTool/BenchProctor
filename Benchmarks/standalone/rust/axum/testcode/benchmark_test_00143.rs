// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00143(headers: HeaderMap) -> impl IntoResponse {
    let referer_value = headers.get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = referer_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    let _cmdline = std::ffi::CString::new(format!("grep {} /var/log/app.log", data)).unwrap_or_default();
    unsafe { libc::system(_cmdline.as_ptr()) };
    Json(serde_json::json!({"count": 0})).into_response()
}
