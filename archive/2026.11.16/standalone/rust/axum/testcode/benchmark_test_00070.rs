// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00070(headers: HeaderMap) -> impl IntoResponse {
    let host_value = headers.get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let _prefix: String = host_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => host_value.to_lowercase(),
        "f" => host_value.to_uppercase(),
        _ => host_value.trim().to_string(),
    };
    tokio::fs::write(format!("/var/app/data/{}", data), "data").await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
