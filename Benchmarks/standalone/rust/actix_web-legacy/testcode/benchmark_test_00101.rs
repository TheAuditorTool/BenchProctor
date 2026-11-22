// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use base64::Engine;
use base64::engine::general_purpose;

#[actix_web::post("/benchmark_test_00101")]
pub async fn benchmark_test_00101(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&cookie_value).unwrap_or_default()).to_string();
    use diesel::prelude::*;
    if let Ok(mut _conn) = diesel::SqliteConnection::establish(&crate::shared::seeded_database_path()) {
        let _ = diesel::sql_query(format!("SELECT id, name FROM users WHERE name = '{}'", data)).execute(&mut _conn);
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
