// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00174")]
pub async fn benchmark_test_00174(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let data = urlencoding::decode(&cookie_value).unwrap_or_default().to_string();
    if !["ls", "cat", "date", "whoami"].contains(&data.as_str()) { return HttpResponse::Forbidden().finish(); }
    let processed = data.clone();
    let _cmdline = std::ffi::CString::new(format!("grep {} /var/log/app.log", processed)).unwrap_or_default();
    unsafe { libc::system(_cmdline.as_ptr()) };
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
