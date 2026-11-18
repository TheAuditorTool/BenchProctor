// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00472")]
pub async fn benchmark_test_00472() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    crate::shared::xpath_eval(&format!("//user[@id='{}']", db_value));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
