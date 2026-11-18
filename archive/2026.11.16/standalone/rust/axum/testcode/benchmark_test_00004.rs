// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00004(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let _prefix: String = raw_body.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => raw_body.to_lowercase(),
        "f" => raw_body.to_uppercase(),
        _ => raw_body.trim().to_string(),
    };
    fn _schema_check(v: &str) -> Result<(), validator::ValidationError> {
        static _RE_SCHEMA: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.\\-]+$").unwrap());
        if _RE_SCHEMA.is_match(v) { Ok(()) } else { Err(validator::ValidationError::new("schema")) }
    }
    #[derive(validator::Validate)]
    struct _SchemaInput<'a> { #[validate(custom(function = "_schema_check"))] value: &'a str }
    use validator::Validate;
    if (_SchemaInput { value: &data }).validate().is_err() { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    crate::shared::store_session("data", &processed);
    Json(serde_json::json!({"count": 0})).into_response()
}
