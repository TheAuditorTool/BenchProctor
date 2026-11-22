// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00142")]
pub async fn benchmark_test_00142() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(env_value.clone());
    crate::shared::set_cookie(&format!("session={}; HttpOnly; SameSite=Strict", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
