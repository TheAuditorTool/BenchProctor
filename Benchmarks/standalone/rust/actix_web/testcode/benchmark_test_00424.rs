// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00424")]
pub async fn benchmark_test_00424(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = ua_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| ua_value.clone());
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.#~\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", processed)).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
