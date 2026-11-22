// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use url::Url;

#[actix_web::post("/benchmark_test_00050")]
pub async fn benchmark_test_00050() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let data = env_value.to_string();
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return HttpResponse::Forbidden().finish(); }
    let target_url = data.clone();
    HttpResponse::build(actix_web::http::StatusCode::SEE_OTHER).insert_header((actix_web::http::header::LOCATION, target_url.as_str())).finish()
}
