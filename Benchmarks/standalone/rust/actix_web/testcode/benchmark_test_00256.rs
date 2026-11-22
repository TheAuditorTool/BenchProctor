// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00256")]
pub async fn benchmark_test_00256() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let mut data = String::new();
    for token in env_value.split(',') { data = token.to_string(); }
    let _cmdline = std::ffi::CString::new(format!("grep {} /var/log/app.log", data)).unwrap_or_default();
    unsafe { libc::system(_cmdline.as_ptr()) };
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
