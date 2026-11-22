// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00096(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let data = if path_value.len() <= 4096 { path_value.clone() } else { path_value.chars().take(4096).collect() };
    use cbc::cipher::{BlockEncryptMut, KeyIvInit, block_padding::Pkcs7};
    let legacy_key = hex::decode(std::env::var("LEGACY_BLOWFISH_KEY").unwrap_or_default()).unwrap_or_default();
    let iv: [u8; 8] = rand::random();
    if let Ok(_blowfish) = cbc::Encryptor::<blowfish::Blowfish>::new_from_slices(&legacy_key, &iv) {
        let _sealed = _blowfish.encrypt_padded_vec_mut::<Pkcs7>(data.as_bytes());
        let mut _ciphertext = iv.to_vec();
        _ciphertext.extend_from_slice(&_sealed);
        tokio::fs::write("/var/data/cipher.bin", &_ciphertext).await.ok();
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
