// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use base64::Engine;
use base64::engine::general_purpose;
use tokio::net::TcpStream;

#[actix_web::post("/benchmark_test_00219")]
pub async fn benchmark_test_00219() -> HttpResponse {
    let msg_value = crate::shared::queue_get_message("app-events");
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&msg_value).unwrap_or_default()).to_string();
    let _sock_host = if data.contains("://") { url::Url::parse(&data).ok().and_then(|u| u.host_str().map(str::to_string)).unwrap_or_default() } else { data.clone() };
    TcpStream::connect(format!("{}:80", _sock_host)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
