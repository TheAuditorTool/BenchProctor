// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use rand::rngs::OsRng;

#[actix_web::post("/benchmark_test_00587")]
pub async fn benchmark_test_00587() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let (payload, _origin) = (db_value.clone(), "http");
    let data = payload;
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
