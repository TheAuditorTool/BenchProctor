// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00225")]
pub async fn benchmark_test_00225() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let (payload, _origin) = (env_value.clone(), "http");
    let data = payload;
    Command::new("sh").arg("-c").arg(format!("cat {}", data)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
