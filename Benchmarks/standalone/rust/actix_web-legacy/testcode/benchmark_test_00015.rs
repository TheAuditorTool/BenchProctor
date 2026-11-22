// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use tokio::net::TcpStream;

#[actix_web::post("/benchmark_test_00015")]
pub async fn benchmark_test_00015(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let _prefix: String = xml_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => xml_value.to_lowercase(),
        "f" => xml_value.to_uppercase(),
        _ => xml_value.trim().to_string(),
    };
    let _sock_host = if data.contains("://") { url::Url::parse(&data).ok().and_then(|u| u.host_str().map(str::to_string)).unwrap_or_default() } else { data.clone() };
    TcpStream::connect(format!("{}:80", _sock_host)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
