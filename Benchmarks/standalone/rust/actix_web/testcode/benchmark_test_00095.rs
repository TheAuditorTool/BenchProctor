// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00095")]
pub async fn benchmark_test_00095(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let mut data = String::new();
    for token in user_id.split(',') { data = token.to_string(); }
    fn _schema_check(v: &str) -> Result<(), validator::ValidationError> {
        static _RE_SCHEMA: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.\\-]+$").unwrap());
        if _RE_SCHEMA.is_match(v) { Ok(()) } else { Err(validator::ValidationError::new("schema")) }
    }
    #[derive(validator::Validate)]
    struct _SchemaInput<'a> { #[validate(custom(function = "_schema_check"))] value: &'a str }
    use validator::Validate;
    if (_SchemaInput { value: &data }).validate().is_err() { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    crate::shared::store_session("data", &processed);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
