// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00003")]
pub async fn benchmark_test_00003(req: HttpRequest) -> HttpResponse {
    let forwarded_ip = req.headers().get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = forwarded_ip.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    crate::shared::store_session("data", &processed);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
