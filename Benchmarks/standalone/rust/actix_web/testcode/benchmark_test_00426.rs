// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00426")]
pub async fn benchmark_test_00426(req: HttpRequest) -> HttpResponse {
    let forwarded_ip = req.headers().get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match forwarded_ip.chars().next() { Some(_) => forwarded_ip.clone(), None => "default".to_string() };
    crate::shared::store_session("data", &data);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
