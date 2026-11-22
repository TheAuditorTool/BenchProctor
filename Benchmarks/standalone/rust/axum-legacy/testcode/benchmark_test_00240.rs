// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00240(headers: HeaderMap) -> impl IntoResponse {
    let ua_value = headers.get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut data = String::new();
    for token in ua_value.split(',') { data = token.to_string(); }
    let _coerced = data.parse::<i64>().unwrap_or(0);
    let processed = _coerced.to_string();
    if let Ok(_conn) = rusqlite::Connection::open(crate::shared::seeded_database_path()) {
        if let Ok(mut _stmt) = _conn.prepare(&format!("SELECT * FROM users WHERE id = {}", processed)) {
            let _ = _stmt.exists([]);
        }
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
