// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00276")]
pub async fn benchmark_test_00276() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let data: String = env_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| env_value.clone());
    use cbc::cipher::{BlockModeEncrypt, KeyIvInit, block_padding::Pkcs7};
    use hmac::Mac;
    let data_key = hex::decode(std::env::var("DATA_ENCRYPTION_KEY").unwrap_or_default()).unwrap_or_default();
    let mac_key = hex::decode(std::env::var("DATA_MAC_KEY").unwrap_or_default()).unwrap_or_default();
    let iv: [u8; 16] = rand::random();
    if let Ok(_aes) = cbc::Encryptor::<aes::Aes256>::new_from_slices(&data_key, &iv) {
        let _sealed = _aes.encrypt_padded_vec::<Pkcs7>(data.as_bytes());
        let mut _ciphertext = iv.to_vec();
        _ciphertext.extend_from_slice(&_sealed);
        if let Ok(mut _mac) = <hmac::Hmac<sha2::Sha256> as hmac::KeyInit>::new_from_slice(&mac_key) {
            _mac.update(&_ciphertext);
            _ciphertext.extend_from_slice(&_mac.finalize().into_bytes());
            tokio::fs::write("/var/data/cipher.bin", &_ciphertext).await.ok();
        }
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
