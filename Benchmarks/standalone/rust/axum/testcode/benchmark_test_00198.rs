// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use std::collections::HashMap;

pub async fn benchmark_test_00198(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let data = if field_value.len() <= 4096 { field_value.clone() } else { field_value.chars().take(4096).collect() };
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.#%\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
