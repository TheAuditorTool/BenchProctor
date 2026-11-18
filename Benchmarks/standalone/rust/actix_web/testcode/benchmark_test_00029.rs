// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use url::Url;

#[actix_web::post("/benchmark_test_00029")]
pub async fn benchmark_test_00029(body: web::Bytes) -> HttpResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let data = serde_json::from_str::<serde_json::Value>(&json_value)
        .ok().and_then(|v| v["value"].as_str().map(|s| s.to_string())).unwrap_or_default();
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return HttpResponse::Forbidden().finish(); }
    let target_url = data.clone();
    HttpResponse::Found().append_header(("Location", target_url.as_str())).finish()
}
