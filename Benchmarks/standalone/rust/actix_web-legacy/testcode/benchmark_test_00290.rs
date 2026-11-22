// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00290")]
pub async fn benchmark_test_00290(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let (payload, _origin) = (user_id.clone(), "http");
    let data = payload;
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    if let Ok(mut _app_context) = crate::shared::APP_CONTEXT.write() {
        _app_context.insert("partner_tier".to_string(), processed.clone());
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
