// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;
use base64::Engine;
use base64::engine::general_purpose;

pub async fn benchmark_test_00055() -> impl IntoResponse {
    let redis_value = redis::Client::open("redis://cache:6379").ok().and_then(|client| client.get_connection().ok()).and_then(|mut conn| redis::cmd("GET").arg("user_data").query::<String>(&mut conn).ok()).unwrap_or_default();
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&redis_value).unwrap_or_default()).to_string();
    if let Ok(_conn) = rusqlite::Connection::open(crate::shared::seeded_database_path()) {
        if let Ok(mut _stmt) = _conn.prepare("SELECT * FROM users WHERE name = :name") {
            let _ = _stmt.exists(rusqlite::named_params! { ":name": data });
        }
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
