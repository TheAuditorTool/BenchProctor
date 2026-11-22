// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use base64::Engine;
use base64::engine::general_purpose;

#[actix_web::post("/benchmark_test_00082")]
pub async fn benchmark_test_00082() -> HttpResponse {
    let redis_value = redis::Client::open("redis://cache:6379").ok().and_then(|client| client.get_connection().ok()).and_then(|mut conn| redis::cmd("GET").arg("user_data").query::<String>(&mut conn).ok()).unwrap_or_default();
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&redis_value).unwrap_or_default()).to_string();
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9_.#\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = '{}'", processed));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
