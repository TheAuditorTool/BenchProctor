// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;
use url::Url;

pub async fn benchmark_test_00148() -> impl IntoResponse {
    let msg_value = crate::shared::queue_get_message("app-events");
    let _prefix: String = msg_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => msg_value.to_lowercase(),
        "f" => msg_value.to_uppercase(),
        _ => msg_value.trim().to_string(),
    };
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let target_url = data.clone();
    if let Ok(_target) = reqwest::Url::parse(&target_url) {
        let _request = reqwest::Request::new(reqwest::Method::GET, _target);
        let _client = reqwest::Client::new();
        _client.execute(_request).await.ok();
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
