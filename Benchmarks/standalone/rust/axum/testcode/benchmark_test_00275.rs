// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00275() -> impl IntoResponse {
    let profile_value = crate::shared::db_fetch_one("SELECT bio FROM profiles LIMIT 1");
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", profile_value).ok();
    let checked_path = format!("/var/app/data/{}", std::path::Path::new(&data).file_name().and_then(|n| n.to_str()).unwrap_or(""));
    tokio::fs::write(&checked_path, "data").await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
