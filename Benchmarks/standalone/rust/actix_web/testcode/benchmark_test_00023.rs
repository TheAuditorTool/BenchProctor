// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00023")]
pub async fn benchmark_test_00023(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    crate::shared::store_session("data", &raw_body);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
