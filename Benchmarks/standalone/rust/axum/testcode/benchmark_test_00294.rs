// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;
use url::Url;

pub async fn benchmark_test_00294(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    struct FormData { payload: String }
    let data = FormData { payload: user_id.clone() }.payload;
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    let _host = parsed.host_str().unwrap_or("").to_string();
    let _addr = std::net::ToSocketAddrs::to_socket_addrs(&(_host.as_str(), 0u16)).ok().and_then(|mut it| it.next()).map(|sa| sa.ip().to_string()).unwrap_or_default();
    static _RE_BLOCK: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)").unwrap());
    if _addr.is_empty() || _RE_BLOCK.is_match(&_addr) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let target_url = data.clone();
    reqwest::get(&target_url).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
