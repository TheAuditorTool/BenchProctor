// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00428")]
pub async fn benchmark_test_00428(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let captured = raw_body.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let processed = shell_escape::escape(std::borrow::Cow::from(&data)).to_string();
    Command::new("sh").arg("-c").arg(format!("cat {}", processed)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
