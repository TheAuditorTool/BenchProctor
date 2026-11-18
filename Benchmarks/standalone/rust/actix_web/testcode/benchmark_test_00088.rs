// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00088")]
pub async fn benchmark_test_00088(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = ua_value.to_string();
    if !["ls", "cat", "date", "whoami"].contains(&data.as_str()) { return HttpResponse::Forbidden().finish(); }
    let processed = data.clone();
    Command::new("bash").arg("-c").arg(format!("echo {}", processed)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
