// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00499")]
pub async fn benchmark_test_00499() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    tokio::fs::remove_file(format!("/var/app/data/{}", env_value)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
