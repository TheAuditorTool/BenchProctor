// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00124")]
pub async fn benchmark_test_00124(req: HttpRequest) -> HttpResponse {
    let forwarded_ip = req.headers().get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", forwarded_ip).ok();
    let Some(at) = data.find('@') else { return HttpResponse::BadRequest().finish(); };
    let mail_domain = &data[at + 1..];
    let _ = mail_domain;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
