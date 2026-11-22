// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00187(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let captured = path_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let _coerced = data.parse::<i64>().unwrap_or(0);
    let processed = _coerced.to_string();
    use diesel::prelude::*;
    if let Ok(mut _conn) = diesel::SqliteConnection::establish(&crate::shared::seeded_database_path()) {
        let _ = diesel::sql_query(format!("SELECT id, name FROM users WHERE id = {}", processed)).execute(&mut _conn);
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
