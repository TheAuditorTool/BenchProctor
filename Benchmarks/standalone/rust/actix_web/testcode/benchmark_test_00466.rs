// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use rand::rngs::OsRng;

#[actix_web::post("/benchmark_test_00466")]
pub async fn benchmark_test_00466() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    struct FormData { payload: String }
    let data = FormData { payload: comment_value.clone() }.payload;
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
