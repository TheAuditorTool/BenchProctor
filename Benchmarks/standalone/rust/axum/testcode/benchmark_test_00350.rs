// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00350() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    crate::shared::xpath_eval(&format!("//user[@id='{}']", db_value));
    Json(serde_json::json!({"count": 0})).into_response()
}
