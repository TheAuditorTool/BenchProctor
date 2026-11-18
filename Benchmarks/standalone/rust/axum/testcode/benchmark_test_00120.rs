// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00120(headers: HeaderMap) -> impl IntoResponse {
    let forwarded_ip = headers.get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = forwarded_ip.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    crate::shared::ldap_search(&format!("uid={}", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
