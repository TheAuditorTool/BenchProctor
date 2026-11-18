// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00568(headers: HeaderMap) -> impl IntoResponse {
    let forwarded_ip = headers.get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = forwarded_ip.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| forwarded_ip.clone());
    crate::shared::store_session("data", &data);
    Json(serde_json::json!({"count": 0})).into_response()
}
