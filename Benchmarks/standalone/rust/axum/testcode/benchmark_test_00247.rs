// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00247(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = raw_body.replace("\t", " ");
    use md5::Digest;
    let _ = md5::Md5::digest(data.as_bytes());
    Json(serde_json::json!({"count": 0})).into_response()
}
