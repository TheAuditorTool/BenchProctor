// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00060(body: Bytes) -> impl IntoResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let captured = xml_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    use sha2::Digest;
    let _ = sha2::Sha256::digest(data.as_bytes());
    Json(serde_json::json!({"count": 0})).into_response()
}
