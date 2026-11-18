// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00123")]
pub async fn benchmark_test_00123(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = if auth_header.len() <= 4096 { auth_header.clone() } else { auth_header.chars().take(4096).collect() };
    Command::new("bash").arg("-c").arg(format!("echo {}", data)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
