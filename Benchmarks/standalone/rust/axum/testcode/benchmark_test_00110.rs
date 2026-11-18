// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00110(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let data = urlencoding::decode(&path_value).unwrap_or_default().to_string();
    let _ciphertext = crate::shared::encrypt(&data);
    tokio::fs::write("/var/data/cipher.bin", _ciphertext.as_bytes()).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
