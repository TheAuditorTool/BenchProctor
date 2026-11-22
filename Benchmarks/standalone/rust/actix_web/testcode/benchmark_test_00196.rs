// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use base64::Engine;
use base64::engine::general_purpose;
use rand::rngs::SysRng;

#[actix_web::post("/benchmark_test_00196")]
pub async fn benchmark_test_00196(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&raw_body).unwrap_or_default()).to_string();
    let _token: u64 = rand::random();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
