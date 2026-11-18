// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00261() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    struct FormData { payload: String }
    let data = FormData { payload: comment_value.clone() }.payload;
    let base = std::path::Path::new("/var/app/data");
    let candidate = tokio::fs::canonicalize(base.join(&data)).await.unwrap_or_default();
    if !candidate.starts_with(base) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let checked_path = candidate.to_string_lossy().to_string();
    tokio::fs::remove_file(&checked_path).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
