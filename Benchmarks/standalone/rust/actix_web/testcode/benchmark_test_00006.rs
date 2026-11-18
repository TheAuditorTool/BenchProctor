// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00006")]
pub async fn benchmark_test_00006() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = match db_value.chars().next() { Some(_) => db_value.clone(), None => "default".to_string() };
    use md5::Digest;
    let _ = md5::Md5::digest(data.as_bytes());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
