// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00536")]
pub async fn benchmark_test_00536() -> HttpResponse {
    let profile_value = crate::shared::db_fetch_one("SELECT bio FROM profiles LIMIT 1");
    let transform = |v: String| v.trim().to_string();
    let data = transform(profile_value.clone());
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = '{}'", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
