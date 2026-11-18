// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::net::TcpStream;

pub async fn benchmark_test_00300() -> impl IntoResponse {
    let redis_value = redis::Client::open("redis://cache:6379").ok().and_then(|client| client.get_connection().ok()).and_then(|mut conn| redis::cmd("GET").arg("user_data").query::<String>(&mut conn).ok()).unwrap_or_default();
    let data = redis_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    let _sock_host = if data.contains("://") { url::Url::parse(&data).ok().and_then(|u| u.host_str().map(str::to_string)).unwrap_or_default() } else { data.clone() };
    TcpStream::connect(format!("{}:80", _sock_host)).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
