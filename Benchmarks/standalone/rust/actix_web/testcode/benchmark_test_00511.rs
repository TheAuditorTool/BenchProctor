// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00511")]
pub async fn benchmark_test_00511(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let captured = header_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    Command::new("echo").arg(&data).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
