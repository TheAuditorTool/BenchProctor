// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00095")]
pub async fn benchmark_test_00095(req: HttpRequest) -> HttpResponse {
    let host_value = req.headers().get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = host_value.to_string();
    use sha1::Digest;
    let _ = sha1::Sha1::new().chain_update(data.as_bytes()).finalize();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
