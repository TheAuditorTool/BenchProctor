// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00231")]
pub async fn benchmark_test_00231(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    struct FormData { payload: String }
    let data = FormData { payload: user_id.clone() }.payload;
    let _bounded = data.parse::<i64>().unwrap_or(0).clamp(0, 2147483647);
    let processed = _bounded.to_string();
    let requested: i64 = processed.parse().unwrap_or(0);
    let count = requested.clamp(0, 4096) as usize;
    let _buf: Vec<u8> = vec![0u8; count];
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
