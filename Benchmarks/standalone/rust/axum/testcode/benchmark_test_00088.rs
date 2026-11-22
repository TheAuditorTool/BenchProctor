// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00088(headers: HeaderMap) -> impl IntoResponse {
    let header_value = headers.get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    struct FormData { payload: String }
    let data = FormData { payload: header_value.clone() }.payload;
    use aes::cipher::{BlockCipherEncrypt, KeyInit};
    let data_key = hex::decode(std::env::var("DATA_ENCRYPTION_KEY").unwrap_or_default()).unwrap_or_default();
    if let Ok(_aes) = aes::Aes256::new_from_slice(&data_key) {
        let mut _ciphertext = data.as_bytes().to_vec();
        let _pad = 16 - _ciphertext.len() % 16;
        _ciphertext.resize(_ciphertext.len() + _pad, _pad as u8);
        for _block in _ciphertext.chunks_exact_mut(16) {
            _aes.encrypt_block(_block.try_into().expect("a 16-byte block"));
        }
        tokio::fs::write("/var/data/cipher.bin", &_ciphertext).await.ok();
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
