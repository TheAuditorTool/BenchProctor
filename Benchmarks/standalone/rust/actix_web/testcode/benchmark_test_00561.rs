// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use base64::Engine;
use base64::engine::general_purpose;

#[actix_web::post("/benchmark_test_00561")]
pub async fn benchmark_test_00561() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&db_value).unwrap_or_default()).to_string();
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.#%\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    crate::shared::ldap_search(&format!("uid={}", processed));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
