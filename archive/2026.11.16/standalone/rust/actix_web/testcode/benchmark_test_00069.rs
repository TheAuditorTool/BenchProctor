// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00069")]
pub async fn benchmark_test_00069(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    Command::new("echo").arg(&cookie_value).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
