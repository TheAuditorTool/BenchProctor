// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00277")]
pub async fn benchmark_test_00277() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = String::from_utf8_lossy(&hex::decode(&db_value).unwrap_or_default()).to_string();
    let base = std::path::Path::new("/var/app/data");
    let candidate = tokio::fs::canonicalize(base.join(&data)).await.unwrap_or_default();
    if !candidate.starts_with(base) { return HttpResponse::Forbidden().finish(); }
    let checked_path = candidate.to_string_lossy().to_string();
    tokio::fs::remove_file(&checked_path).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
