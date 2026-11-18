// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;

pub async fn benchmark_test_00092(headers: HeaderMap) -> impl IntoResponse {
    let auth_header = headers.get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = auth_header.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.#%\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
