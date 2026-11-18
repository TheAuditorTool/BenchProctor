// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00376() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = match comment_value.chars().next() { Some(_) => comment_value.clone(), None => "default".to_string() };
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", data)).await;
    Json(serde_json::json!({"count": 0})).into_response()
}
