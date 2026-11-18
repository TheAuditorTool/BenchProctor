// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00135")]
pub async fn benchmark_test_00135(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let _prefix: String = header_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => header_value.to_lowercase(),
        "f" => header_value.to_uppercase(),
        _ => header_value.trim().to_string(),
    };
    let _ciphertext = crate::shared::encrypt(&data);
    tokio::fs::write("/var/data/cipher.bin", _ciphertext.as_bytes()).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
