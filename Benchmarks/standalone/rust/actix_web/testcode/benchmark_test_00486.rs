// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00486")]
pub async fn benchmark_test_00486() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = comment_value.replace("\t", " ");
    use sha2::Digest;
    let _ = sha2::Sha256::digest(data.as_bytes());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
