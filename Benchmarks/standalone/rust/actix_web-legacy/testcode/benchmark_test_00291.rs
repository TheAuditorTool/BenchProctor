// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use base64::Engine;
use base64::engine::general_purpose;

#[actix_web::post("/benchmark_test_00291")]
pub async fn benchmark_test_00291() -> HttpResponse {
    let redis_value = redis::Client::open("redis://cache:6379").ok().and_then(|client| client.get_connection().ok()).and_then(|mut conn| redis::cmd("GET").arg("user_data").query::<String>(&mut conn).ok()).unwrap_or_default();
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&redis_value).unwrap_or_default()).to_string();
    if let Ok(_conn) = rusqlite::Connection::open(crate::shared::seeded_database_path()) {
        if let Ok(mut _stmt) = _conn.prepare("SELECT * FROM users WHERE name = :name") {
            let _ = _stmt.exists(rusqlite::named_params! { ":name": data });
        }
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
