// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00142(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = String::from_utf8_lossy(raw_body.as_bytes()).to_string();
    if let Ok(_conn) = rusqlite::Connection::open(crate::shared::seeded_database_path()) {
        if let Ok(mut _stmt) = _conn.prepare(&format!("SELECT * FROM users WHERE name = '{}'", data)) {
            let _ = _stmt.exists([]);
        }
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
