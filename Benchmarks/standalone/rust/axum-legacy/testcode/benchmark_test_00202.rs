// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00202(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let data = path_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    let rows: u32 = data.parse().unwrap_or(0);
    let _records: Vec<u8> = Vec::with_capacity((rows * 512) as usize);
    Json(serde_json::json!({"count": 0})).into_response()
}
