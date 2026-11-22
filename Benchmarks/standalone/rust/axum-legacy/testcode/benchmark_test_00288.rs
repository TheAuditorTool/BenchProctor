// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00288(headers: HeaderMap) -> impl IntoResponse {
    let header_value = headers.get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match header_value.chars().next() { Some(_) => header_value.clone(), None => "default".to_string() };
    use aes_gcm::aead::{Aead, KeyInit};
    let data_key = hex::decode(std::env::var("DATA_ENCRYPTION_KEY").unwrap_or_default()).unwrap_or_default();
    if let Ok(_gcm) = aes_gcm::Aes256Gcm::new_from_slice(&data_key) {
        let _nonce: [u8; 12] = rand::random();
        let mut _ciphertext = _nonce.to_vec();
        _ciphertext.extend(_gcm.encrypt(aes_gcm::Nonce::from_slice(&_nonce), data.as_bytes()).unwrap_or_default());
        tokio::fs::write("/var/data/cipher.bin", &_ciphertext).await.ok();
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
