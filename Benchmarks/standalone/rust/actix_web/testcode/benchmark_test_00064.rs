// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use url::Url;

#[actix_web::post("/benchmark_test_00064/{id}")]
pub async fn benchmark_test_00064(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let data = if path_value.len() <= 4096 { path_value.clone() } else { path_value.chars().take(4096).collect() };
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return HttpResponse::Forbidden().finish(); }
    let target_url = data.clone();
    HttpResponse::Found().append_header(("Location", target_url.as_str())).finish()
}
