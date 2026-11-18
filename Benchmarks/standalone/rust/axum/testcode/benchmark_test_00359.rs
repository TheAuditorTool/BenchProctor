// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00359() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let transform = |v: String| v.trim().to_string();
    let data = transform(env_value.clone());
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
