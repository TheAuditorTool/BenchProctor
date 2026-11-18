// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use tokio::net::TcpStream;
use url::Url;

#[actix_web::post("/benchmark_test_00022")]
pub async fn benchmark_test_00022() -> HttpResponse {
    let msg_value = crate::shared::queue_get_message("app-events");
    struct FormData { payload: String }
    let data = FormData { payload: msg_value.clone() }.payload;
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return HttpResponse::Forbidden().finish(); }
    let target_url = data.clone();
    let _sock_host = if target_url.contains("://") { url::Url::parse(&target_url).ok().and_then(|u| u.host_str().map(str::to_string)).unwrap_or_default() } else { target_url.clone() };
    TcpStream::connect(format!("{}:80", _sock_host)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
