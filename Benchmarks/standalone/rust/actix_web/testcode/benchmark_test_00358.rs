// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00358")]
pub async fn benchmark_test_00358(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(raw_body.clone());
    crate::shared::set_cookie(&format!("session={}; Secure; HttpOnly; SameSite=Strict", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
