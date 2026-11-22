// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00049")]
pub async fn benchmark_test_00049(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = referer_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    let _cmdline = std::ffi::CString::new(format!("grep {} /var/log/app.log", data)).unwrap_or_default();
    unsafe { libc::system(_cmdline.as_ptr()) };
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
