// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00203/{id}")]
pub async fn benchmark_test_00203(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let _prefix: String = path_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => path_value.to_lowercase(),
        "f" => path_value.to_uppercase(),
        _ => path_value.trim().to_string(),
    };
    use aes_gcm::aead::{Aead, KeyInit};
    let data_key = hex::decode(std::env::var("DATA_ENCRYPTION_KEY").unwrap_or_default()).unwrap_or_default();
    if let Ok(_gcm) = aes_gcm::Aes256Gcm::new_from_slice(&data_key) {
        let _nonce: [u8; 12] = rand::random();
        let mut _ciphertext = _nonce.to_vec();
        _ciphertext.extend(_gcm.encrypt(&_nonce.into(), data.as_bytes()).unwrap_or_default());
        tokio::fs::write("/var/data/cipher.bin", &_ciphertext).await.ok();
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
