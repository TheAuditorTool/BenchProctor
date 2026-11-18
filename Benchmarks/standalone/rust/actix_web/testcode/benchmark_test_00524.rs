// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00524")]
pub async fn benchmark_test_00524() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = comment_value.to_string();
    if !["config.json", "index.html", "readme.md"].contains(&data.as_str()) { return HttpResponse::Forbidden().finish(); }
    let checked_path = format!("/var/app/data/{}", data);
    let _ = tokio::fs::read_to_string(&checked_path).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
