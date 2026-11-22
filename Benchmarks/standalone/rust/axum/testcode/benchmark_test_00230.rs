// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00230() -> impl IntoResponse {
    let profile_value = crate::shared::db_fetch_one("SELECT bio FROM profiles LIMIT 1");
    let mut pending: std::collections::VecDeque<String> = profile_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    let base = std::path::Path::new("/var/app/data");
    let candidate = tokio::fs::canonicalize(base.join(&data)).await.unwrap_or_default();
    if !candidate.starts_with(base) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let checked_path = candidate.to_string_lossy().to_string();
    tokio::fs::write(&checked_path, "data").await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
