// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00222")]
pub async fn benchmark_test_00222(req: HttpRequest) -> HttpResponse {
    let forwarded_ip = req.headers().get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut pending: std::collections::VecDeque<String> = forwarded_ip.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    let _bounded = data.parse::<i64>().unwrap_or(0).clamp(0, 2147483647);
    let processed = _bounded.to_string();
    let rows: u32 = processed.parse().unwrap_or(0);
    let Some(_capacity) = rows.checked_mul(512).filter(|bytes| *bytes <= 1 << 21) else { return HttpResponse::BadRequest().finish(); };
    let _records: Vec<u8> = Vec::with_capacity(_capacity as usize);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
