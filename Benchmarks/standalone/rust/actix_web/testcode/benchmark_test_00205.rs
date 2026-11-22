// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use rand::rngs::SysRng;

#[actix_web::post("/benchmark_test_00205")]
pub async fn benchmark_test_00205() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = if db_value.len() <= 4096 { db_value.clone() } else { db_value.chars().take(4096).collect() };
    let _token: u64 = rand::random();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
