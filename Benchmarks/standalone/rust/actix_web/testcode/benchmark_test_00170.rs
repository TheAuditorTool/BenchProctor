// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00170")]
pub async fn benchmark_test_00170(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(auth_header.clone());
    if let Ok(_conn) = rusqlite::Connection::open(crate::shared::seeded_database_path()) {
        if let Ok(mut _stmt) = _conn.prepare("SELECT * FROM users WHERE name = :name") {
            let _ = _stmt.exists(rusqlite::named_params! { ":name": data });
        }
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
