// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00034(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let multipart_value = {
        let mut _mv = String::new();
        if let Ok(Some(_field)) = multipart.next_field().await {
            _mv = _field.text().await.unwrap_or_default();
        }
        _mv
    };
    let data = multipart_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    use aes::cipher::{BlockEncrypt, KeyInit};
    let data_key = hex::decode(std::env::var("DATA_ENCRYPTION_KEY").unwrap_or_default()).unwrap_or_default();
    if let Ok(_aes) = aes::Aes256::new_from_slice(&data_key) {
        let mut _ciphertext = data.as_bytes().to_vec();
        let _pad = 16 - _ciphertext.len() % 16;
        _ciphertext.resize(_ciphertext.len() + _pad, _pad as u8);
        for _block in _ciphertext.chunks_exact_mut(16) {
            _aes.encrypt_block(aes::cipher::generic_array::GenericArray::from_mut_slice(_block));
        }
        tokio::fs::write("/var/data/cipher.bin", &_ciphertext).await.ok();
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
