// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use base64::Engine;
use base64::engine::general_purpose;

#[actix_web::post("/benchmark_test_00178")]
pub async fn benchmark_test_00178() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&db_value).unwrap_or_default()).to_string();
    if !["config.json", "index.html", "readme.md"].contains(&data.as_str()) { return HttpResponse::Forbidden().finish(); }
    let checked_path = format!("/var/app/data/{}", data);
    tokio::fs::write(&checked_path, "data").await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
