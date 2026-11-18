// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00141")]
pub async fn benchmark_test_00141() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let (payload, _origin) = (comment_value.clone(), "http");
    let data = payload;
    use cbc::cipher::{BlockEncryptMut, KeyIvInit, block_padding::Pkcs7};
    let legacy_key = hex::decode(std::env::var("LEGACY_3DES_KEY").unwrap_or_default()).unwrap_or_default();
    let iv: [u8; 8] = rand::random();
    let _ciphertext = cbc::Encryptor::<des::TdesEde3>::new_from_slices(&legacy_key, &iv).map(|c| c.encrypt_padded_vec_mut::<Pkcs7>(data.as_bytes())).unwrap_or_default();
    tokio::fs::write("/var/data/cipher.bin", &_ciphertext).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
