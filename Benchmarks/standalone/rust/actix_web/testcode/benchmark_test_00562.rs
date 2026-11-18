// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use url::Url;

#[actix_web::post("/benchmark_test_00562")]
pub async fn benchmark_test_00562(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let mut data = String::new();
    for token in field_value.split(',') { data = token.to_string(); }
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return HttpResponse::Forbidden().finish(); }
    let target_url = data.clone();
    HttpResponse::Found().append_header(("Location", target_url.as_str())).finish()
}
