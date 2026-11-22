// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00166")]
pub async fn benchmark_test_00166(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let data = xml_value.to_string();
    let quantity: u32 = data.parse().unwrap_or(0);
    let total_cents = quantity * 1299;
    crate::shared::db_exec_bind("INSERT INTO logs (data) VALUES ($1)", &total_cents.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
