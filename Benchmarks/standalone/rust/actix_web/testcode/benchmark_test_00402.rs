// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00402")]
pub async fn benchmark_test_00402(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let mut data = String::new();
    for token in user_id.split(',') { data = token.to_string(); }
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.%~\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    crate::shared::xpath_eval(&format!("//user[@id='{}']", processed));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
