// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00082")]
pub async fn benchmark_test_00082() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let transform = |v: String| v.trim().to_string();
    let data = transform(comment_value.clone());
    if let Ok(_conn) = rusqlite::Connection::open(crate::shared::seeded_database_path()) {
        if let Ok(mut _stmt) = _conn.prepare(&format!("SELECT * FROM users WHERE name = '{}'", data)) {
            let _ = _stmt.exists([]);
        }
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
