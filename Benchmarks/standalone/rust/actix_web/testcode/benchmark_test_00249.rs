// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00249")]
pub async fn benchmark_test_00249(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match ua_value.chars().next() { Some(_) => ua_value.clone(), None => "default".to_string() };
    let _bounded = data.parse::<i64>().unwrap_or(0).clamp(0, 2147483647);
    let processed = _bounded.to_string();
    let requested: i64 = processed.parse().unwrap_or(0);
    let count = requested.clamp(0, 4096) as usize;
    let _buf: Vec<u8> = vec![0u8; count];
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
