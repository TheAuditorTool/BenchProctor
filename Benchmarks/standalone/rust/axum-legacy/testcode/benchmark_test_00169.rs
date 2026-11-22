// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00169(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let data = urlencoding::decode(&path_value).unwrap_or_default().to_string();
    use sha2::Digest;
    let mut _hasher = sha2::Sha256::new();
    _hasher.update(data.as_bytes());
    let _ = _hasher.finalize();
    Json(serde_json::json!({"count": 0})).into_response()
}
