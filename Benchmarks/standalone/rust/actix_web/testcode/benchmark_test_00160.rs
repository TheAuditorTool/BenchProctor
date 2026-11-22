// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use url::Url;

#[actix_web::post("/benchmark_test_00160")]
pub async fn benchmark_test_00160() -> HttpResponse {
    let api_value = crate::shared::fetch_url("https://api.partner.example.com/v1/records");
    let _prefix: String = api_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => api_value.to_lowercase(),
        "f" => api_value.to_uppercase(),
        _ => api_value.trim().to_string(),
    };
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return HttpResponse::Forbidden().finish(); }
    let target_url = data.clone();
    HttpResponse::build(actix_web::http::StatusCode::SEE_OTHER).insert_header((actix_web::http::header::LOCATION, target_url.as_str())).finish()
}
