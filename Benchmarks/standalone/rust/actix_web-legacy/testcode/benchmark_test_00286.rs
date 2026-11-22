// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use url::Url;

#[actix_web::post("/benchmark_test_00286/{id}")]
pub async fn benchmark_test_00286(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let mut data = String::new();
    for token in path_value.split(',') { data = token.to_string(); }
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return HttpResponse::Forbidden().finish(); }
    let target_url = data.clone();
    HttpResponse::build(actix_web::http::StatusCode::SEE_OTHER).insert_header((actix_web::http::header::LOCATION, target_url.as_str())).finish()
}
