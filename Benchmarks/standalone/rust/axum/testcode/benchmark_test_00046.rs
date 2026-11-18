// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00046(headers: HeaderMap) -> impl IntoResponse {
    let host_value = headers.get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = host_value.to_string();
    crate::shared::store_session("data", &data);
    Json(serde_json::json!({"count": 0})).into_response()
}
