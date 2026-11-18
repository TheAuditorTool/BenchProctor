// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00432")]
pub async fn benchmark_test_00432() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", db_value).ok();
    use cbc::cipher::{BlockEncryptMut, KeyIvInit, block_padding::Pkcs7};
    let legacy_key = hex::decode(std::env::var("LEGACY_3DES_KEY").unwrap_or_default()).unwrap_or_default();
    let iv: [u8; 8] = rand::random();
    let _ciphertext = cbc::Encryptor::<des::TdesEde3>::new_from_slices(&legacy_key, &iv).map(|c| c.encrypt_padded_vec_mut::<Pkcs7>(data.as_bytes())).unwrap_or_default();
    tokio::fs::write("/var/data/cipher.bin", &_ciphertext).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
