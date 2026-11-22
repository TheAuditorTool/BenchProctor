// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00270(headers: HeaderMap) -> impl IntoResponse {
    let header_value = headers.get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = header_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| header_value.clone());
    if let Ok(_target) = reqwest::Url::parse(&data) {
        let _request = reqwest::Request::new(reqwest::Method::GET, _target);
        let _client = reqwest::Client::new();
        _client.execute(_request).await.ok();
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
