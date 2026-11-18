// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00103")]
pub async fn benchmark_test_00103(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let data = field_value.replace("\t", " ");
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9_.#\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = '{}'", processed));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
