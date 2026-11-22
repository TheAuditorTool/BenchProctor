// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00167(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let multipart_value = {
        let mut _mv = String::new();
        if let Ok(Some(_field)) = multipart.next_field().await {
            _mv = _field.text().await.unwrap_or_default();
        }
        _mv
    };
    let mut pending: std::collections::VecDeque<String> = multipart_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    use cbc::cipher::{BlockEncryptMut, KeyIvInit, block_padding::Pkcs7};
    use hmac::Mac;
    let data_key = hex::decode(std::env::var("DATA_ENCRYPTION_KEY").unwrap_or_default()).unwrap_or_default();
    let mac_key = hex::decode(std::env::var("DATA_MAC_KEY").unwrap_or_default()).unwrap_or_default();
    let iv: [u8; 16] = rand::random();
    if let Ok(_aes) = cbc::Encryptor::<aes::Aes256>::new_from_slices(&data_key, &iv) {
        let _sealed = _aes.encrypt_padded_vec_mut::<Pkcs7>(data.as_bytes());
        let mut _ciphertext = iv.to_vec();
        _ciphertext.extend_from_slice(&_sealed);
        if let Ok(mut _mac) = <hmac::Hmac<sha2::Sha256> as Mac>::new_from_slice(&mac_key) {
            _mac.update(&_ciphertext);
            _ciphertext.extend_from_slice(&_mac.finalize().into_bytes());
            tokio::fs::write("/var/data/cipher.bin", &_ciphertext).await.ok();
        }
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
