// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00277")]
pub async fn benchmark_test_00277(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match referer_value.chars().next() { Some(_) => referer_value.clone(), None => "default".to_string() };
    let Some(at) = data.find('@') else { return HttpResponse::BadRequest().finish(); };
    let mail_domain = &data[at + 1..];
    let _ = mail_domain;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
