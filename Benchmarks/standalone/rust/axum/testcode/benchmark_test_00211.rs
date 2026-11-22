// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;

pub async fn benchmark_test_00211(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(field_value.clone());
    let processed = shell_escape::escape(std::borrow::Cow::from(&data)).to_string();
    let _cmdline = std::ffi::CString::new(format!("grep {} /var/log/app.log", processed)).unwrap_or_default();
    unsafe { libc::system(_cmdline.as_ptr()) };
    Json(serde_json::json!({"count": 0})).into_response()
}
