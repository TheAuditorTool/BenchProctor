// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00125")]
pub async fn benchmark_test_00125(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = ua_value.replace("\t", " ");
    use sha2::Digest;
    let _ = sha2::Sha256::new().chain_update(data.as_bytes()).finalize();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
