// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00226")]
pub async fn benchmark_test_00226() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let transform = |v: String| v.trim().to_string();
    let data = transform(env_value.clone());
    use sha2::Digest;
    let _ = sha2::Sha256::new().chain_update(data.as_bytes()).finalize();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
