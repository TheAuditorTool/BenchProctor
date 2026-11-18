// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00052")]
pub async fn benchmark_test_00052(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = raw_body.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = '{}'", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
