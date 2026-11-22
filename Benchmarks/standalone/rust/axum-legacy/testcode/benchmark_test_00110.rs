// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use url::Url;

pub async fn benchmark_test_00110(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let mut data = String::new();
    for token in path_value.split(',') { data = token.to_string(); }
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let target_url = data.clone();
    (StatusCode::FOUND, [(axum::http::header::LOCATION, target_url.clone())]).into_response()
}
