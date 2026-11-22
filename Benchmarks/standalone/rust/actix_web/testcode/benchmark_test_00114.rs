// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00114")]
pub async fn benchmark_test_00114(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let data: String = field_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| field_value.clone());
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.#~\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", processed)).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
