// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00198")]
pub async fn benchmark_test_00198() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    struct FormData { payload: String }
    let data = FormData { payload: comment_value.clone() }.payload;
    let base = std::path::Path::new("/var/app/data");
    let candidate = tokio::fs::canonicalize(base.join(&data)).await.unwrap_or_default();
    if !candidate.starts_with(base) { return HttpResponse::Forbidden().finish(); }
    let checked_path = candidate.to_string_lossy().to_string();
    tokio::fs::remove_file(&checked_path).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
