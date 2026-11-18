// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00041(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let data = path_value.replace("\t", " ");
    crate::shared::store_session("data", &data);
    Json(serde_json::json!({"count": 0})).into_response()
}
