// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00016")]
pub async fn benchmark_test_00016(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let data = String::from_utf8_lossy(&hex::decode(&user_id).unwrap_or_default()).to_string();
    if let Ok(_conn) = rusqlite::Connection::open(crate::shared::seeded_database_path()) {
        if let Ok(mut _stmt) = _conn.prepare("SELECT * FROM users WHERE name = :name") {
            let _ = _stmt.exists(rusqlite::named_params! { ":name": data });
        }
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
