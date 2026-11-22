// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00261")]
pub async fn benchmark_test_00261(req: HttpRequest) -> HttpResponse {
    let origin_value = req.headers().get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match origin_value.chars().next() { Some(_) => origin_value.clone(), None => "default".to_string() };
    let quantity: u32 = data.parse().unwrap_or(0);
    let total_cents = quantity * 1299;
    crate::shared::db_exec_bind("INSERT INTO logs (data) VALUES ($1)", &total_cents.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
