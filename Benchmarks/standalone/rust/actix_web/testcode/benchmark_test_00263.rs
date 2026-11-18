// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00263")]
pub async fn benchmark_test_00263(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let result: Option<String> = std::env::var(header_value.as_str()).ok();
    let value = match result { Some(v) => v, None => return HttpResponse::NotFound().finish() };
    let _ = value;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
