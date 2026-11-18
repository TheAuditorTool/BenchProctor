// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00043")]
pub async fn benchmark_test_00043() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let data = env_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    let _coerced = matches!(data.to_lowercase().as_str(), "true" | "1" | "yes" | "on");
    let processed = _coerced.to_string();
    crate::shared::store_session("data", &processed);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
