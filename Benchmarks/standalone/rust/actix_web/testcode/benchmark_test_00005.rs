// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00005")]
pub async fn benchmark_test_00005(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let data = String::from_utf8_lossy(&hex::decode(&cookie_value).unwrap_or_default()).to_string();
    Command::new("sh").arg("-c").arg(format!("grep {} /var/log/app.log", data)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
