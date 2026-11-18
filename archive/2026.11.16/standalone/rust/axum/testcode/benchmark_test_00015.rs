// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;
use base64::Engine;
use base64::engine::general_purpose;

pub async fn benchmark_test_00015() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&db_value).unwrap_or_default()).to_string();
    crate::shared::store_session("data", &data);
    Json(serde_json::json!({"count": 0})).into_response()
}
