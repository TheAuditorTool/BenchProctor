// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use url::Url;

pub async fn benchmark_test_00014(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let parsed = Url::parse(&path_value).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let target_url = path_value.clone();
    axum::response::Redirect::to(target_url.as_str()).into_response()
}
