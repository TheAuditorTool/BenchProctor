// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00031(headers: HeaderMap) -> impl IntoResponse {
    let origin_value = headers.get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let _prefix: String = origin_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => origin_value.to_lowercase(),
        "f" => origin_value.to_uppercase(),
        _ => origin_value.trim().to_string(),
    };
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
