// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00055(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = match raw_body.chars().next() { Some(_) => raw_body.clone(), None => "default".to_string() };
    use diesel::prelude::*;
    if let Ok(mut _conn) = diesel::SqliteConnection::establish(&crate::shared::seeded_database_path()) {
        let _ = diesel::sql_query("SELECT id, name FROM users WHERE name = ?").bind::<diesel::sql_types::Text, _>(data.clone()).execute(&mut _conn);
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
