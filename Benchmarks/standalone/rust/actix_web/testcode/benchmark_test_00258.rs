// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00258")]
pub async fn benchmark_test_00258() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let data = match env_value.chars().next() { Some(_) => env_value.clone(), None => "default".to_string() };
    if !["ls", "cat", "date", "whoami"].contains(&data.as_str()) { return HttpResponse::Forbidden().finish(); }
    let processed = data.clone();
    Command::new("sh").arg("-c").arg(format!("cat {}", processed)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
