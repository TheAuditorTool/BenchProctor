// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use tokio::net::TcpStream;

#[actix_web::post("/benchmark_test_00257")]
pub async fn benchmark_test_00257() -> HttpResponse {
    let msg_value = crate::shared::queue_get_message("app-events");
    let _prefix: String = msg_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => msg_value.to_lowercase(),
        "f" => msg_value.to_uppercase(),
        _ => msg_value.trim().to_string(),
    };
    let _sock_host = if data.contains("://") { url::Url::parse(&data).ok().and_then(|u| u.host_str().map(str::to_string)).unwrap_or_default() } else { data.clone() };
    TcpStream::connect(format!("{}:80", _sock_host)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
