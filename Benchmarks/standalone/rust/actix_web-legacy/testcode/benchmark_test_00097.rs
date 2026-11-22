// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00097")]
pub async fn benchmark_test_00097() -> HttpResponse {
    let msg_value = crate::shared::queue_get_message("app-events");
    let mut data = String::new();
    for token in msg_value.split(',') { data = token.to_string(); }
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    crate::shared::db_query(&format!("SELECT * FROM users ORDER BY {}", processed));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
