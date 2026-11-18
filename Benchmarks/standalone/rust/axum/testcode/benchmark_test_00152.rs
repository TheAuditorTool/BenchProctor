// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00152() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = comment_value.to_string();
    if !["config.json", "index.html", "readme.md"].contains(&data.as_str()) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let checked_path = format!("/var/app/data/{}", data);
    let _ = tokio::fs::read_to_string(&checked_path).await;
    Json(serde_json::json!({"count": 0})).into_response()
}
