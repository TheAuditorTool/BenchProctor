// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00406() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.%~\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&comment_value) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = comment_value.clone();
    crate::shared::xpath_eval(&format!("//user[@id='{}']", processed));
    Json(serde_json::json!({"count": 0})).into_response()
}
