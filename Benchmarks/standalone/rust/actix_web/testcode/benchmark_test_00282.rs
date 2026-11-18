// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00282")]
pub async fn benchmark_test_00282(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", xml_value).ok();
    let _ciphertext = crate::shared::encrypt(&data);
    tokio::fs::write("/var/data/cipher.bin", _ciphertext.as_bytes()).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
