// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use tokio::net::TcpStream;

#[actix_web::post("/benchmark_test_00080")]
pub async fn benchmark_test_00080(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", xml_value).ok();
    let _sock_host = if data.contains("://") { url::Url::parse(&data).ok().and_then(|u| u.host_str().map(str::to_string)).unwrap_or_default() } else { data.clone() };
    TcpStream::connect(format!("{}:80", _sock_host)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
