// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::net::TcpStream;

pub async fn benchmark_test_00342() -> impl IntoResponse {
    let msg_value = crate::shared::queue_get_message("app-events");
    struct FormData { payload: String }
    let data = FormData { payload: msg_value.clone() }.payload;
    let _sock_host = if data.contains("://") { url::Url::parse(&data).ok().and_then(|u| u.host_str().map(str::to_string)).unwrap_or_default() } else { data.clone() };
    TcpStream::connect(format!("{}:80", _sock_host)).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
