// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00220() -> impl IntoResponse {
    let file_value = tokio::fs::read_to_string("/tmp/data").await.unwrap_or_default();
    let data = file_value.replace("\t", " ");
    use diesel::prelude::*;
    if let Ok(mut _conn) = diesel::SqliteConnection::establish(&crate::shared::seeded_database_path()) {
        let _ = diesel::sql_query("SELECT id, name FROM users WHERE name = ?").bind::<diesel::sql_types::Text, _>(data.clone()).execute(&mut _conn);
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
