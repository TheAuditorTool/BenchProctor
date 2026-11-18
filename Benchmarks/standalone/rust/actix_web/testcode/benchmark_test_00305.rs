// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00305")]
pub async fn benchmark_test_00305(req: HttpRequest) -> HttpResponse {
    let origin_value = req.headers().get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut pending: std::collections::VecDeque<String> = origin_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    tokio::fs::remove_file(format!("/var/app/data/{}", processed)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
