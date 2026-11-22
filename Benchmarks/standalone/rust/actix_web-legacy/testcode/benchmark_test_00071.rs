// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use rand::rngs::OsRng;

#[actix_web::post("/benchmark_test_00071")]
pub async fn benchmark_test_00071(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data: String = raw_body.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| raw_body.clone());
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
