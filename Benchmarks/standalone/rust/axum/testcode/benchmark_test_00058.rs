// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00058() -> impl IntoResponse {
    let file_value = tokio::fs::read_to_string("/tmp/data").await.unwrap_or_default();
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9_.#\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&file_value) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = file_value.clone();
    if let Ok(_conn) = rusqlite::Connection::open(crate::shared::seeded_database_path()) {
        if let Ok(mut _stmt) = _conn.prepare(&format!("SELECT * FROM users WHERE name = '{}'", processed)) {
            let _ = _stmt.exists([]);
        }
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
