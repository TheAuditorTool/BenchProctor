// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00016(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let data: String = path_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| path_value.clone());
    tokio::fs::write(format!("/var/app/data/{}", data), "data").await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
