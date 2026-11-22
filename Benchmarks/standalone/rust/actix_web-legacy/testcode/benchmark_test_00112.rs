// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00112")]
pub async fn benchmark_test_00112(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    tokio::process::Command::new("grep").arg("-e").arg(&raw_body).arg("/var/log/app.log").output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
