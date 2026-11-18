// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00007() -> impl IntoResponse {
    let profile_value = crate::shared::db_fetch_one("SELECT bio FROM profiles LIMIT 1");
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", profile_value)).await;
    Json(serde_json::json!({"count": 0})).into_response()
}
