// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use rand::rngs::OsRng;

#[actix_web::post("/benchmark_test_00213")]
pub async fn benchmark_test_00213() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = comment_value.to_string();
    use rand::RngCore;
    let mut _rng = rand::rngs::OsRng;
    let _token = _rng.next_u64();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
