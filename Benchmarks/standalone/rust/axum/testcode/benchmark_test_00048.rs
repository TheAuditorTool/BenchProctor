// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00048(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let multipart_value = {
        let mut _mv = String::new();
        if let Ok(Some(_field)) = multipart.next_field().await {
            _mv = _field.text().await.unwrap_or_default();
        }
        _mv
    };
    let data = multipart_value.to_string();
    use cbc::cipher::{BlockModeEncrypt, KeyIvInit, block_padding::Pkcs7};
    let legacy_key = hex::decode(std::env::var("LEGACY_BLOWFISH_KEY").unwrap_or_default()).unwrap_or_default();
    let iv: [u8; 8] = rand::random();
    if let Ok(_blowfish) = cbc::Encryptor::<blowfish::Blowfish>::new_from_slices(&legacy_key, &iv) {
        let _sealed = _blowfish.encrypt_padded_vec::<Pkcs7>(data.as_bytes());
        let mut _ciphertext = iv.to_vec();
        _ciphertext.extend_from_slice(&_sealed);
        tokio::fs::write("/var/data/cipher.bin", &_ciphertext).await.ok();
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
