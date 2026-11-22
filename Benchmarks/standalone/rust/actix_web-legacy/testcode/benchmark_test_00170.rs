// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00170")]
pub async fn benchmark_test_00170(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut data = String::new();
    for token in header_value.split(',') { data = token.to_string(); }
    use diesel::prelude::*;
    if let Ok(mut _conn) = diesel::SqliteConnection::establish(&crate::shared::seeded_database_path()) {
        let _ = diesel::sql_query("SELECT id, name FROM users WHERE name = ?").bind::<diesel::sql_types::Text, _>(data.clone()).execute(&mut _conn);
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
