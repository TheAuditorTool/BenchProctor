// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00201(headers: HeaderMap) -> impl IntoResponse {
    let header_value = headers.get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut data = String::new();
    for token in header_value.split(',') { data = token.to_string(); }
    let _ciphertext = crate::shared::encrypt(&data);
    tokio::fs::write("/var/data/cipher.bin", _ciphertext.as_bytes()).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
