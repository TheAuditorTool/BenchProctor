// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00205")]
pub async fn benchmark_test_00205() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = match comment_value.chars().next() { Some(_) => comment_value.clone(), None => "default".to_string() };
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", data)).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
