// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00105")]
pub async fn benchmark_test_00105(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut data = String::new();
    for token in header_value.split(',') { data = token.to_string(); }
    let _ciphertext = crate::shared::encrypt(&data);
    tokio::fs::write("/var/data/cipher.bin", _ciphertext.as_bytes()).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
