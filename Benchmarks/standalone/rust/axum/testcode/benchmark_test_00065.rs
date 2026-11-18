// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00065() -> impl IntoResponse {
    let file_value = tokio::fs::read_to_string("/tmp/data").await.unwrap_or_default();
    let transform = |v: String| v.trim().to_string();
    let data = transform(file_value.clone());
    crate::shared::db_query(&format!("SELECT * FROM `{}`", data.replace('`', "")));
    Json(serde_json::json!({"count": 0})).into_response()
}
