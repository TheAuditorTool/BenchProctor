// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00041(headers: HeaderMap) -> impl IntoResponse {
    let auth_header = headers.get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match auth_header.chars().next() { Some(_) => auth_header.clone(), None => "default".to_string() };
    reqwest::get(&data).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
