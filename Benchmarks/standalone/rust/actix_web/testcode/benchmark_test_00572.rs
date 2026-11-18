// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00572")]
pub async fn benchmark_test_00572() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", env_value).ok();
    Command::new("sh").arg("-c").arg(format!("grep {} /var/log/app.log", data)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
