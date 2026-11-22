// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00263")]
pub async fn benchmark_test_00263(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(field_value.clone());
    let processed = shell_escape::escape(std::borrow::Cow::from(&data)).to_string();
    let _cmdline = std::ffi::CString::new(format!("grep {} /var/log/app.log", processed)).unwrap_or_default();
    unsafe { libc::system(_cmdline.as_ptr()) };
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
