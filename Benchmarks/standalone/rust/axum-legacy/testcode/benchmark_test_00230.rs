// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00230() -> impl IntoResponse {
    let profile_value = crate::shared::db_fetch_one("SELECT bio FROM profiles LIMIT 1");
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(profile_value.clone());
    let base_dir = "/var/app/data";
    let full_path = tokio::fs::canonicalize(format!("{}/{}", base_dir, data)).await.unwrap_or_default();
    if !full_path.starts_with(base_dir) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let checked_path = full_path.to_string_lossy().to_string();
    tokio::fs::remove_file(&checked_path).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
