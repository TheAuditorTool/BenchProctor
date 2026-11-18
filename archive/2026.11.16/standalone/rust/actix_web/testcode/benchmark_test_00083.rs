// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00083")]
pub async fn benchmark_test_00083(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", ua_value).ok();
    Command::new("bash").arg("-c").arg(format!("echo {}", data)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
