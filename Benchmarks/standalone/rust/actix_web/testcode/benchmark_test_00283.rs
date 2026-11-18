// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00283")]
pub async fn benchmark_test_00283() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = db_value.replace("\t", " ");
    let _bounded = data.parse::<i64>().unwrap_or(0).clamp(0, 2147483647);
    let processed = _bounded.to_string();
    let requested: i64 = processed.parse().unwrap_or(0);
    let count = requested.clamp(0, 4096) as usize;
    let _buf: Vec<u8> = vec![0u8; count];
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
