// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use std::collections::HashMap;

pub async fn benchmark_test_00114(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    let captured = user_id.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.#%\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
