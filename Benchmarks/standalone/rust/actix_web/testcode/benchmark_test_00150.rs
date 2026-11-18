// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use tokio::net::TcpStream;

#[actix_web::post("/benchmark_test_00150")]
pub async fn benchmark_test_00150() -> HttpResponse {
    let msg_value = crate::shared::queue_get_message("app-events");
    let data = msg_value.replace("\t", " ");
    let _sock_host = if data.contains("://") { url::Url::parse(&data).ok().and_then(|u| u.host_str().map(str::to_string)).unwrap_or_default() } else { data.clone() };
    TcpStream::connect(format!("{}:80", _sock_host)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
