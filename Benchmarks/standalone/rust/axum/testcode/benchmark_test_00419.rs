// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use std::collections::HashMap;
use url::Url;

pub async fn benchmark_test_00419(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let mut data = String::new();
    for token in field_value.split(',') { data = token.to_string(); }
    let parsed = Url::parse(&data).unwrap_or_else(|_| Url::parse("http://invalid").unwrap());
    static _RE_HOST: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(api\\.priv\\.local|cdn\\.edgecdn\\.io)$").unwrap());
    if !_RE_HOST.is_match(parsed.host_str().unwrap_or("")) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let target_url = data.clone();
    axum::response::Redirect::to(target_url.as_str()).into_response()
}
