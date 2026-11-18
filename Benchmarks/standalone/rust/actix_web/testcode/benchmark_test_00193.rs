// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00193")]
pub async fn benchmark_test_00193() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = comment_value.to_string();
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = match result { Some(v) => v, None => return HttpResponse::NotFound().finish() };
    let _ = value;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
