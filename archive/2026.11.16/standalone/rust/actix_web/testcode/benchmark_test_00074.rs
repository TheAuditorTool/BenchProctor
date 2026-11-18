// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00074")]
pub async fn benchmark_test_00074(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    use sha2::Digest;
    let _ = sha2::Sha256::digest(xml_value.as_bytes());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
