// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00071() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = String::from_utf8_lossy(&hex::decode(&db_value).unwrap_or_default()).to_string();
    crate::shared::set_cookie(&format!("session={}; HttpOnly; SameSite=Strict", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
