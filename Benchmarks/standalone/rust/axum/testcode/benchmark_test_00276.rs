// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;
use base64::Engine;
use base64::engine::general_purpose;

pub async fn benchmark_test_00276() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&db_value).unwrap_or_default()).to_string();
    if !["config.json", "index.html", "readme.md"].contains(&data.as_str()) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let checked_path = format!("/var/app/data/{}", data);
    tokio::fs::write(&checked_path, "data").await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
