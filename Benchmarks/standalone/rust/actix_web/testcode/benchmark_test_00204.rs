// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use url::Url;

#[actix_web::post("/benchmark_test_00204")]
pub async fn benchmark_test_00204(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = raw_body.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return HttpResponse::Forbidden().finish(); }
    let target_url = data.clone();
    reqwest::get(&target_url).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
