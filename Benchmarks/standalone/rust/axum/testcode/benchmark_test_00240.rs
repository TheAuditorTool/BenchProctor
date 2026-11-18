// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;
use base64::Engine;
use base64::engine::general_purpose;

pub async fn benchmark_test_00240(headers: HeaderMap) -> impl IntoResponse {
    let auth_header = headers.get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&auth_header).unwrap_or_default()).to_string();
    crate::shared::xpath_eval(&format!("//user[@id='{}']", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
