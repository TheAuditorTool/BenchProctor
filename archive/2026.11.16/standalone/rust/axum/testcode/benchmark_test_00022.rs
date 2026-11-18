// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00022(body: Bytes) -> impl IntoResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    use sha2::Digest;
    let _ = sha2::Sha256::digest(xml_value.as_bytes());
    Json(serde_json::json!({"count": 0})).into_response()
}
