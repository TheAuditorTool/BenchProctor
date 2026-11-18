// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00255(headers: HeaderMap) -> impl IntoResponse {
    let origin_value = headers.get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = if origin_value.len() <= 4096 { origin_value.clone() } else { origin_value.chars().take(4096).collect() };
    crate::shared::xpath_eval(&format!("//user[@id='{}']", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
