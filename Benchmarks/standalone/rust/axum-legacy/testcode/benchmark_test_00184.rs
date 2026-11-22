// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00184() -> impl IntoResponse {
    let file_value = tokio::fs::read_to_string("/tmp/data").await.unwrap_or_default();
    let mut data = String::new();
    for token in file_value.split(',') { data = token.to_string(); }
    use diesel::prelude::*;
    if let Ok(mut _conn) = diesel::SqliteConnection::establish(&crate::shared::seeded_database_path()) {
        let _ = diesel::sql_query(format!("SELECT id, name FROM users WHERE name = '{}'", data)).execute(&mut _conn);
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
