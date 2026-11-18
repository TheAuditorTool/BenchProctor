// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00394")]
pub async fn benchmark_test_00394() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", env_value).ok();
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = '{}'", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
