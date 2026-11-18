// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00008")]
pub async fn benchmark_test_00008() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let (payload, _origin) = (env_value.clone(), "http");
    let data = payload;
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = result.unwrap();
    let _ = value;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
