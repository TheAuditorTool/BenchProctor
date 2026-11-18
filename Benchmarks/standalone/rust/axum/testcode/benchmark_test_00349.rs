// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;
use base64::Engine;
use base64::engine::general_purpose;

pub async fn benchmark_test_00349() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&db_value).unwrap_or_default()).to_string();
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.#%\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    crate::shared::ldap_search(&format!("uid={}", processed));
    Json(serde_json::json!({"count": 0})).into_response()
}
