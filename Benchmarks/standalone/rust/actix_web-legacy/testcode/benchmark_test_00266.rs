// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00266")]
pub async fn benchmark_test_00266(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    struct FormData { payload: String }
    let data = FormData { payload: referer_value.clone() }.payload;
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
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
