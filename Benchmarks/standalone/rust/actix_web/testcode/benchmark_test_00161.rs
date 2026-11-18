// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00161")]
pub async fn benchmark_test_00161() -> HttpResponse {
    let profile_value = crate::shared::db_fetch_one("SELECT bio FROM profiles LIMIT 1");
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", profile_value).ok();
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = '{}'", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
