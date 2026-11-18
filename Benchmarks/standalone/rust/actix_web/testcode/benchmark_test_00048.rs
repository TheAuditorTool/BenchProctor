// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00048")]
pub async fn benchmark_test_00048() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let data = if env_value.len() <= 4096 { env_value.clone() } else { env_value.chars().take(4096).collect() };
    Command::new("bash").arg("-c").arg(format!("echo {}", data)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
