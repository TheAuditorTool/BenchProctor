// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00100(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let multipart_value = {
        let mut _mv = String::new();
        if let Ok(Some(_field)) = multipart.next_field().await {
            _mv = _field.text().await.unwrap_or_default();
        }
        _mv
    };
    let data = urlencoding::decode(&multipart_value).unwrap_or_default().to_string();
    use aes_gcm::aead::{Aead, KeyInit};
    let data_key = hex::decode(std::env::var("DATA_ENCRYPTION_KEY").unwrap_or_default()).unwrap_or_default();
    if let Ok(_gcm) = aes_gcm::Aes256Gcm::new_from_slice(&data_key) {
        let _nonce: [u8; 12] = rand::random();
        let mut _ciphertext = _nonce.to_vec();
        _ciphertext.extend(_gcm.encrypt(&_nonce.into(), data.as_bytes()).unwrap_or_default());
        tokio::fs::write("/var/data/cipher.bin", &_ciphertext).await.ok();
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
