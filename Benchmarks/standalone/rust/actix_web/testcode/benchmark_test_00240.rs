// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00240")]
pub async fn benchmark_test_00240() -> HttpResponse {
    let file_value = tokio::fs::read_to_string("/tmp/data").await.unwrap_or_default();
    let mut data = String::new();
    for token in file_value.split(',') { data = token.to_string(); }
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = '{}'", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
