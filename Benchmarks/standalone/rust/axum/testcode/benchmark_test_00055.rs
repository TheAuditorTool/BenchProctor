// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use std::collections::HashMap;

pub async fn benchmark_test_00055(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let data = urlencoding::decode(&field_value).unwrap_or_default().to_string();
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
