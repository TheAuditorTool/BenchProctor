// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00479")]
pub async fn benchmark_test_00479() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = if comment_value.len() <= 4096 { comment_value.clone() } else { comment_value.chars().take(4096).collect() };
    crate::shared::db_query_bind("SELECT * FROM users WHERE id = $1", &data);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
