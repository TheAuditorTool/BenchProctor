// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00101")]
pub async fn benchmark_test_00101(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.%\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&header_value) { return HttpResponse::BadRequest().finish(); }
    let processed = header_value.clone();
    Command::new("sh").arg("-c").arg(format!("cat {}", processed)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
