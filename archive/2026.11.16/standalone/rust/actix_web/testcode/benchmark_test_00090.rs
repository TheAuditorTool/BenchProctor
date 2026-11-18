// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00090")]
pub async fn benchmark_test_00090(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = if header_value.len() <= 4096 { header_value.clone() } else { header_value.chars().take(4096).collect() };
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    crate::shared::ldap_search(&format!("uid={}", processed));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
