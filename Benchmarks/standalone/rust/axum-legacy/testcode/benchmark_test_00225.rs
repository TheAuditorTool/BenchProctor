// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;
use base64::Engine;
use base64::engine::general_purpose;

pub async fn benchmark_test_00225(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&raw_body).unwrap_or_default()).to_string();
    let _cmdline = std::ffi::CString::new(format!("grep {} /var/log/app.log", data)).unwrap_or_default();
    unsafe { libc::system(_cmdline.as_ptr()) };
    Json(serde_json::json!({"count": 0})).into_response()
}
