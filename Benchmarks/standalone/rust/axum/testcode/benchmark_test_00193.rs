// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00193(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    struct FormData { payload: String }
    let data = FormData { payload: path_value.clone() }.payload;
    let requested: u32 = data.parse().unwrap_or(0);
    let count = (requested * 4096) as usize;
    let _buf: Vec<u8> = vec![0u8; count];
    Json(serde_json::json!({"count": 0})).into_response()
}
