// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00223(headers: HeaderMap) -> impl IntoResponse {
    let auth_header = headers.get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(auth_header.clone());
    if let Ok(_conn) = rusqlite::Connection::open(crate::shared::seeded_database_path()) {
        if let Ok(mut _stmt) = _conn.prepare("SELECT * FROM users WHERE name = :name") {
            let _ = _stmt.exists(rusqlite::named_params! { ":name": data });
        }
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
