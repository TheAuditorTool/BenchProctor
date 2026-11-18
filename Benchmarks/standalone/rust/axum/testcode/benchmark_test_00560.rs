// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use url::Url;

pub async fn benchmark_test_00560(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = String::from_utf8_lossy(raw_body.as_bytes()).to_string();
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let target_url = data.clone();
    axum::response::Redirect::to(target_url.as_str()).into_response()
}
