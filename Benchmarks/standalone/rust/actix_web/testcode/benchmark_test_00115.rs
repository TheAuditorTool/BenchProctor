// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00115")]
pub async fn benchmark_test_00115() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", db_value).ok();
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
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
