// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00495(body: Bytes) -> impl IntoResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let data = match json_value.chars().next() { Some(_) => json_value.clone(), None => "default".to_string() };
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    crate::shared::xpath_eval(&format!("//user[@id='{}']", processed));
    Json(serde_json::json!({"count": 0})).into_response()
}
