// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00110")]
pub async fn benchmark_test_00110() -> HttpResponse {
    let profile_value = crate::shared::db_fetch_one("SELECT bio FROM profiles LIMIT 1");
    let data = profile_value.to_string();
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    if let Ok(_conn) = rusqlite::Connection::open(crate::shared::seeded_database_path()) {
        if let Ok(mut _stmt) = _conn.prepare(&format!("SELECT * FROM users ORDER BY {}", processed)) {
            let _ = _stmt.exists([]);
        }
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
