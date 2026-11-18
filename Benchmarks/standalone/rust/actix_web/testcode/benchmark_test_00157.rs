// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00157/{id}")]
pub async fn benchmark_test_00157(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let _bounded = path_value.parse::<i64>().unwrap_or(0).clamp(0, 2147483647);
    let processed = _bounded.to_string();
    let requested: i64 = processed.parse().unwrap_or(0);
    let count = requested.clamp(0, 4096) as usize;
    let _buf: Vec<u8> = vec![0u8; count];
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
