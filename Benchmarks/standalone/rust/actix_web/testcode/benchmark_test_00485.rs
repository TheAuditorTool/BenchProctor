// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00485")]
pub async fn benchmark_test_00485(req: HttpRequest) -> HttpResponse {
    let host_value = req.headers().get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let captured = host_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    use sha2::Digest;
    let _ = sha2::Sha256::digest(data.as_bytes());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
