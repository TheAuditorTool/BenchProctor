// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00183() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let transform = |v: String| v.trim().to_string();
    let data = transform(comment_value.clone());
    if let Ok(_conn) = rusqlite::Connection::open(crate::shared::seeded_database_path()) {
        if let Ok(mut _stmt) = _conn.prepare(&format!("SELECT * FROM users WHERE name = '{}'", data)) {
            let _ = _stmt.exists([]);
        }
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
