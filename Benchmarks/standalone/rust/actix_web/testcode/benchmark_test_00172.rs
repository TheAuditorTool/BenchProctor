// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::net::TcpStream;

#[actix_web::post("/benchmark_test_00172")]
pub async fn benchmark_test_00172(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match auth_header.chars().next() { Some(_) => auth_header.clone(), None => "default".to_string() };
    let _sock_host = if data.contains("://") { url::Url::parse(&data).ok().and_then(|u| u.host_str().map(str::to_string)).unwrap_or_default() } else { data.clone() };
    TcpStream::connect(format!("{}:80", _sock_host)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
