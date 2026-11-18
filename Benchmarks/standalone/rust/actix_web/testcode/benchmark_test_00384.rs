// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00384")]
pub async fn benchmark_test_00384(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut data = String::new();
    for token in ua_value.split(',') { data = token.to_string(); }
    Command::new("bash").arg("-c").arg(format!("echo {}", data)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
