// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00139")]
pub async fn benchmark_test_00139(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = String::from_utf8_lossy(raw_body.as_bytes()).to_string();
    if let Ok(_conn) = rusqlite::Connection::open(crate::shared::seeded_database_path()) {
        if let Ok(mut _stmt) = _conn.prepare(&format!("SELECT * FROM users WHERE name = '{}'", data)) {
            let _ = _stmt.exists([]);
        }
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
