// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00489")]
pub async fn benchmark_test_00489(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let (payload, _origin) = (auth_header.clone(), "http");
    let data = payload;
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.%~\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    crate::shared::xpath_eval(&format!("//user[@id='{}']", processed));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
