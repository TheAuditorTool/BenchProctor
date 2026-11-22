// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00004")]
pub async fn benchmark_test_00004(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let mut pending: std::collections::VecDeque<String> = cookie_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    use cbc::cipher::{BlockModeEncrypt, KeyIvInit, block_padding::Pkcs7};
    let legacy_key = hex::decode(std::env::var("LEGACY_BLOWFISH_KEY").unwrap_or_default()).unwrap_or_default();
    let iv: [u8; 8] = rand::random();
    if let Ok(_blowfish) = cbc::Encryptor::<blowfish::Blowfish>::new_from_slices(&legacy_key, &iv) {
        let _sealed = _blowfish.encrypt_padded_vec::<Pkcs7>(data.as_bytes());
        let mut _ciphertext = iv.to_vec();
        _ciphertext.extend_from_slice(&_sealed);
        tokio::fs::write("/var/data/cipher.bin", &_ciphertext).await.ok();
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
