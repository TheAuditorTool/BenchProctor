// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;

pub async fn benchmark_test_00207() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let (payload, _origin) = (db_value.clone(), "http");
    let data = payload;
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.#%\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    let _chunk = format!("<div>{}</div>", processed);
    return ([("content-type", "text/html; charset=utf-8")], axum::body::Body::from_stream(futures_util::stream::once(async move { Ok::<_, std::convert::Infallible>(_chunk) }))).into_response();
}
