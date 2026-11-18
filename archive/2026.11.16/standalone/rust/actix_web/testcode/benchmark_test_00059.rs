// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use base64::Engine;
use base64::engine::general_purpose;

#[actix_web::post("/benchmark_test_00059")]
pub async fn benchmark_test_00059(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&raw_body).unwrap_or_default()).to_string();
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = match result { Some(v) => v, None => return HttpResponse::NotFound().finish() };
    let _ = value;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
