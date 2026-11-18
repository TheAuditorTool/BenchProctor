// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00490")]
pub async fn benchmark_test_00490(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = String::from_utf8_lossy(&hex::decode(&header_value).unwrap_or_default()).to_string();
    Command::new("sh").arg("-c").arg(format!("grep {} /var/log/app.log", data)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
