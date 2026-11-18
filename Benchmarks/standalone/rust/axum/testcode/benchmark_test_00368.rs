// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::net::TcpStream;

pub async fn benchmark_test_00368(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let data = if path_value.len() <= 4096 { path_value.clone() } else { path_value.chars().take(4096).collect() };
    let _sock_host = if data.contains("://") { url::Url::parse(&data).ok().and_then(|u| u.host_str().map(str::to_string)).unwrap_or_default() } else { data.clone() };
    TcpStream::connect(format!("{}:80", _sock_host)).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
