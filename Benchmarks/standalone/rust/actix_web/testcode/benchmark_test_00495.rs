// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00495")]
pub async fn benchmark_test_00495() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    crate::shared::set_cookie(&format!("session={}; Secure; HttpOnly; SameSite=Strict", comment_value));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
