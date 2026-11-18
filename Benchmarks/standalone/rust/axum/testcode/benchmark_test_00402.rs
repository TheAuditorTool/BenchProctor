// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00402(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let captured = path_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    use md5::Digest;
    let _ = md5::Md5::digest(data.as_bytes());
    Json(serde_json::json!({"count": 0})).into_response()
}
