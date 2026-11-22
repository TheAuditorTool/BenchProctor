// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00122(headers: HeaderMap) -> impl IntoResponse {
    let forwarded_ip = headers.get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let _profile = std::collections::BTreeMap::from([("display_name".to_string(), forwarded_ip.clone()), ("profile_complete".to_string(), "true".to_string())]);
    if let Ok(mut _session) = crate::shared::SESSION_STORE.lock() {
        _session.extend(_profile);
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
