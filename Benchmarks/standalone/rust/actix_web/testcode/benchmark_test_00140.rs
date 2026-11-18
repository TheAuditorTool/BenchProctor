// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00140")]
pub async fn benchmark_test_00140() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(comment_value.clone());
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = result.unwrap();
    let _ = value;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
