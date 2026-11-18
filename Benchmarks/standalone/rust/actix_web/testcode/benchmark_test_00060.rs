// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00060")]
pub async fn benchmark_test_00060() -> HttpResponse {
    let config_value = tokio::fs::read_to_string("/etc/app/config.json").await.unwrap_or_default();
    let mut data = String::new();
    for token in config_value.split(',') { data = token.to_string(); }
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = '{}'", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
