// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00186() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let data: String = env_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| env_value.clone());
    use cbc::cipher::{BlockEncryptMut, KeyIvInit, block_padding::Pkcs7};
    let legacy_key = hex::decode(std::env::var("LEGACY_3DES_KEY").unwrap_or_default()).unwrap_or_default();
    let iv: [u8; 8] = rand::random();
    let _ciphertext = cbc::Encryptor::<des::TdesEde3>::new_from_slices(&legacy_key, &iv).map(|c| c.encrypt_padded_vec_mut::<Pkcs7>(data.as_bytes())).unwrap_or_default();
    tokio::fs::write("/var/data/cipher.bin", &_ciphertext).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
