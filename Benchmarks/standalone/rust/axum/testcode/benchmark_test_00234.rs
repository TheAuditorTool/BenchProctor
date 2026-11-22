// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00234(body: Bytes) -> impl IntoResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let data = xml_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    use md5::Digest;
    let mut _hasher = md5::Md5::new();
    _hasher.update(data.as_bytes());
    let _ = _hasher.finalize();
    Json(serde_json::json!({"count": 0})).into_response()
}
