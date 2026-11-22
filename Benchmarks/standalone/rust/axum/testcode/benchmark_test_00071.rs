// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00071() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(db_value.clone());
    tokio::fs::write(format!("/var/app/data/{}", data), "data").await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
