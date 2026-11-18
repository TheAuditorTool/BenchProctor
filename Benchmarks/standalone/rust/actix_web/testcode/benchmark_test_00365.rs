// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00365")]
pub async fn benchmark_test_00365() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data: String = db_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| db_value.clone());
    let checked_path = format!("/var/app/data/{}", std::path::Path::new(&data).file_name().and_then(|n| n.to_str()).unwrap_or(""));
    tokio::fs::write(&checked_path, "data").await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
