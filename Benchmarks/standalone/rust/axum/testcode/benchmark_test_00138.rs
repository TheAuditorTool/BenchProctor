// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00138() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let mut pending: std::collections::VecDeque<String> = comment_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = result.unwrap();
    let _ = value;
    Json(serde_json::json!({"count": 0})).into_response()
}
