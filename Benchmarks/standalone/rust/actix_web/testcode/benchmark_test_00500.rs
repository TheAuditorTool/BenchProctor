// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00500")]
pub async fn benchmark_test_00500(req: HttpRequest) -> HttpResponse {
    let host_value = req.headers().get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let captured = host_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let _ciphertext = crate::shared::encrypt(&data);
    tokio::fs::write("/var/data/cipher.bin", _ciphertext.as_bytes()).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
