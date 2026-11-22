// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00190(headers: HeaderMap) -> impl IntoResponse {
    let host_value = headers.get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    fn _schema_check(v: &str) -> Result<(), validator::ValidationError> {
        static _RE_SCHEMA: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.\\-]+$").unwrap());
        if _RE_SCHEMA.is_match(v) { Ok(()) } else { Err(validator::ValidationError::new("schema")) }
    }
    #[derive(validator::Validate)]
    struct _SchemaInput<'a> { #[validate(custom(function = "_schema_check"))] value: &'a str }
    use validator::Validate;
    if (_SchemaInput { value: &host_value }).validate().is_err() { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = host_value.clone();
    let _profile = std::collections::BTreeMap::from([("display_name".to_string(), processed.clone()), ("profile_complete".to_string(), "true".to_string())]);
    if let Ok(mut _session) = crate::shared::SESSION_STORE.lock() {
        _session.extend(_profile);
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
