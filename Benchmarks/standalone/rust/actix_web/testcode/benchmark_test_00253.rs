// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use rand::rngs::SysRng;

#[actix_web::post("/benchmark_test_00253")]
pub async fn benchmark_test_00253(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(header_value.clone());
    use rand::TryRng;
    let _token: u64 = SysRng.try_next_u64().expect("OS randomness unavailable");
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
