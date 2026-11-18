// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00246(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", path_value).ok();
    use sha2::Digest;
    let _ = sha2::Sha256::digest(data.as_bytes());
    Json(serde_json::json!({"count": 0})).into_response()
}
