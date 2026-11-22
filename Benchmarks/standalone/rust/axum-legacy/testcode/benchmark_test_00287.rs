// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00287(headers: HeaderMap) -> impl IntoResponse {
    let ua_value = headers.get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let _prefix: String = ua_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => ua_value.to_lowercase(),
        "f" => ua_value.to_uppercase(),
        _ => ua_value.trim().to_string(),
    };
    let plan_limits: std::collections::HashMap<&str, u32> = std::collections::HashMap::from([("free", 3), ("team", 25), ("enterprise", 500)]);
    let seat_limit = plan_limits.get(data.as_str()).copied().unwrap();
    let _ = seat_limit;
    Json(serde_json::json!({"count": 0})).into_response()
}
