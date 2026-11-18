// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00004(headers: HeaderMap) -> impl IntoResponse {
    let ua_value = headers.get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.%\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&ua_value) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = ua_value.clone();
    Command::new("sh").arg("-c").arg(format!("grep {} /var/log/app.log", processed)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
