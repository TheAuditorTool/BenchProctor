// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00267")]
pub async fn benchmark_test_00267(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = raw_body.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    let processed = shell_escape::escape(std::borrow::Cow::from(&data)).to_string();
    Command::new("sh").arg("-c").arg(format!("grep {} /var/log/app.log", processed)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
