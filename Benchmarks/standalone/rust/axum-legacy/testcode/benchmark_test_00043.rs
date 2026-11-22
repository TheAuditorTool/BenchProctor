// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00043(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let data: String = path_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| path_value.clone());
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = result.unwrap();
    let _ = value;
    Json(serde_json::json!({"count": 0})).into_response()
}
