// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00019(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let (payload, _origin) = (path_value.clone(), "http");
    let data = payload;
    reqwest::get(&data).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
