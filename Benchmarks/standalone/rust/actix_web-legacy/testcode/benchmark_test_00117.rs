// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use rand::rngs::OsRng;

#[actix_web::post("/benchmark_test_00117")]
pub async fn benchmark_test_00117() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let _prefix: String = env_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => env_value.to_lowercase(),
        "f" => env_value.to_uppercase(),
        _ => env_value.trim().to_string(),
    };
    let _token: u64 = rand::random();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
