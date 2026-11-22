// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00246() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = if comment_value.len() <= 4096 { comment_value.clone() } else { comment_value.chars().take(4096).collect() };
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", data)).await;
    Json(serde_json::json!({"count": 0})).into_response()
}
