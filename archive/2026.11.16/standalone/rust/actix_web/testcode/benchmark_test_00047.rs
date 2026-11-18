// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00047")]
pub async fn benchmark_test_00047(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = if raw_body.len() <= 4096 { raw_body.clone() } else { raw_body.chars().take(4096).collect() };
    Command::new("sh").arg("-c").arg(format!("grep {} /var/log/app.log", data)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
