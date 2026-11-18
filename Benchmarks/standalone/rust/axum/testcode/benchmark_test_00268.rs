// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;
use tokio::process::Command;

pub async fn benchmark_test_00268(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let mut data = String::new();
    for token in field_value.split(',') { data = token.to_string(); }
    fn _schema_check(v: &str) -> Result<(), validator::ValidationError> {
        static _RE_SCHEMA: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.%\\-]+$").unwrap());
        if _RE_SCHEMA.is_match(v) { Ok(()) } else { Err(validator::ValidationError::new("schema")) }
    }
    #[derive(validator::Validate)]
    struct _SchemaInput<'a> { #[validate(custom(function = "_schema_check"))] value: &'a str }
    use validator::Validate;
    if (_SchemaInput { value: &data }).validate().is_err() { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    Command::new("bash").arg("-c").arg(format!("echo {}", processed)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
