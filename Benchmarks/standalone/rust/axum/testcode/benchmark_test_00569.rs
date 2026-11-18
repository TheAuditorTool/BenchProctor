// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;

pub async fn benchmark_test_00569(headers: HeaderMap) -> impl IntoResponse {
    let referer_value = headers.get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match referer_value.chars().next() { Some(_) => referer_value.clone(), None => "default".to_string() };
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
