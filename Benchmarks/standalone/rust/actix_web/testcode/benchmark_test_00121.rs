// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use url::Url;

#[actix_web::post("/benchmark_test_00121")]
pub async fn benchmark_test_00121() -> HttpResponse {
    let api_value = crate::shared::fetch_url("https://api.partner.example.com/v1/records");
    let data = api_value.replace("\t", " ");
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return HttpResponse::Forbidden().finish(); }
    let target_url = data.clone();
    if let Ok(_target) = reqwest::Url::parse(&target_url) {
        let _request = reqwest::Request::new(reqwest::Method::GET, _target);
        let _client = reqwest::Client::new();
        _client.execute(_request).await.ok();
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
