// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00175")]
pub async fn benchmark_test_00175(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut pending: std::collections::VecDeque<String> = header_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    let rows: u32 = data.parse().unwrap_or(0);
    let _records: Vec<u8> = Vec::with_capacity((rows * 512) as usize);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
