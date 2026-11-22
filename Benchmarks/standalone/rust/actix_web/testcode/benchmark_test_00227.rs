// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00227")]
pub async fn benchmark_test_00227(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let mut data = String::new();
    for token in user_id.split(',') { data = token.to_string(); }
    let _bounded = data.parse::<i64>().unwrap_or(0).clamp(0, 2147483647);
    let processed = _bounded.to_string();
    let rows: u32 = processed.parse().unwrap_or(0);
    let Some(_capacity) = rows.checked_mul(512).filter(|bytes| *bytes <= 1 << 21) else { return HttpResponse::BadRequest().finish(); };
    let _records: Vec<u8> = Vec::with_capacity(_capacity as usize);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
