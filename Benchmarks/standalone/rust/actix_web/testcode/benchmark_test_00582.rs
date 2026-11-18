// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00582")]
pub async fn benchmark_test_00582() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", db_value).ok();
    crate::shared::xpath_eval(&format!("//user[@id='{}']", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
