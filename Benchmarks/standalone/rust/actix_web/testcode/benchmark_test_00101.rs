// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00101")]
pub async fn benchmark_test_00101() -> HttpResponse {
    let file_value = tokio::fs::read_to_string("/tmp/data").await.unwrap_or_default();
    let data = String::from_utf8_lossy(file_value.as_bytes()).to_string();
    use diesel::prelude::*;
    if let Ok(mut _conn) = diesel::SqliteConnection::establish(&crate::shared::seeded_database_path()) {
        let _ = diesel::sql_query(format!("SELECT id, name FROM users WHERE name = '{}'", data)).execute(&mut _conn);
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
