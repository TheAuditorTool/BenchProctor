// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00561(headers: HeaderMap) -> impl IntoResponse {
    let forwarded_ip = headers.get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match forwarded_ip.chars().next() { Some(_) => forwarded_ip.clone(), None => "default".to_string() };
    crate::shared::store_session("data", &data);
    Json(serde_json::json!({"count": 0})).into_response()
}
