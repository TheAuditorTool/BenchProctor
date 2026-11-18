// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00286")]
pub async fn benchmark_test_00286() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = match comment_value.chars().next() { Some(_) => comment_value.clone(), None => "default".to_string() };
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    crate::shared::ldap_search(&format!("uid={}", processed));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
