// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00163() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let mut pending: std::collections::VecDeque<String> = db_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = match result { Some(v) => v, None => return (StatusCode::NOT_FOUND, "").into_response() };
    let _ = value;
    Json(serde_json::json!({"count": 0})).into_response()
}
