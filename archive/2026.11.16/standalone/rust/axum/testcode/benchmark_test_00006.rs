// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00006(headers: HeaderMap) -> impl IntoResponse {
    let referer_value = headers.get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut pending: std::collections::VecDeque<String> = referer_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    let _coerced = matches!(data.to_lowercase().as_str(), "true" | "1" | "yes" | "on");
    let processed = _coerced.to_string();
    crate::shared::xpath_eval(&format!("//user[@id='{}']", processed));
    Json(serde_json::json!({"count": 0})).into_response()
}
