// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00190")]
pub async fn benchmark_test_00190(req: HttpRequest) -> HttpResponse {
    let forwarded_ip = req.headers().get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(forwarded_ip.clone());
    let quantity: u32 = data.parse().unwrap_or(0);
    let total_cents = quantity * 1299;
    crate::shared::db_exec_bind("INSERT INTO logs (data) VALUES ($1)", &total_cents.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
