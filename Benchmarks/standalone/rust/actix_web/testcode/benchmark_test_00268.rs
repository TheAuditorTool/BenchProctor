// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00268")]
pub async fn benchmark_test_00268(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = serde_json::from_str::<serde_json::Value>(&raw_body)
        .ok().and_then(|v| v["value"].as_str().map(|s| s.to_string())).unwrap_or_default();
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9_.#\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    use diesel::prelude::*;
    if let Ok(mut _conn) = diesel::SqliteConnection::establish(&crate::shared::seeded_database_path()) {
        let _ = diesel::sql_query(format!("SELECT id, name FROM users WHERE name = '{}'", processed)).execute(&mut _conn);
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
