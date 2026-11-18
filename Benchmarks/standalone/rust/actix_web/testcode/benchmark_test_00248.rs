// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use tokio::net::TcpStream;
use url::Url;

#[actix_web::post("/benchmark_test_00248")]
pub async fn benchmark_test_00248() -> HttpResponse {
    let redis_value = redis::Client::open("redis://cache:6379").ok().and_then(|client| client.get_connection().ok()).and_then(|mut conn| redis::cmd("GET").arg("user_data").query::<String>(&mut conn).ok()).unwrap_or_default();
    let data = match redis_value.chars().next() { Some(_) => redis_value.clone(), None => "default".to_string() };
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    let _host = parsed.host_str().unwrap_or("").to_string();
    let _addr = std::net::ToSocketAddrs::to_socket_addrs(&(_host.as_str(), 0u16)).ok().and_then(|mut it| it.next()).map(|sa| sa.ip().to_string()).unwrap_or_default();
    static _RE_BLOCK: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)").unwrap());
    if _addr.is_empty() || _RE_BLOCK.is_match(&_addr) { return HttpResponse::Forbidden().finish(); }
    let target_url = data.clone();
    let _sock_host = if target_url.contains("://") { url::Url::parse(&target_url).ok().and_then(|u| u.host_str().map(str::to_string)).unwrap_or_default() } else { target_url.clone() };
    TcpStream::connect(format!("{}:80", _sock_host)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
