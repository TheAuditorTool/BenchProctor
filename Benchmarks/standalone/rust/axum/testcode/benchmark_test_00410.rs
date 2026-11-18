// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00410() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    crate::shared::set_cookie(&format!("session={}; Secure; HttpOnly; SameSite=Strict", comment_value));
    Json(serde_json::json!({"count": 0})).into_response()
}
