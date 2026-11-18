// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00400() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = if db_value.len() <= 4096 { db_value.clone() } else { db_value.chars().take(4096).collect() };
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = match result { Some(v) => v, None => return (StatusCode::NOT_FOUND, "").into_response() };
    let _ = value;
    Json(serde_json::json!({"count": 0})).into_response()
}
