// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00272/{id}")]
pub async fn benchmark_test_00272(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", path_value).ok();
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.%\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    Command::new("sh").arg("-c").arg(format!("cat {}", processed)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
