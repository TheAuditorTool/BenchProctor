// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00482")]
pub async fn benchmark_test_00482() -> HttpResponse {
    let file_value = tokio::fs::read_to_string("/tmp/data").await.unwrap_or_default();
    let data = if file_value.len() <= 4096 { file_value.clone() } else { file_value.chars().take(4096).collect() };
    crate::shared::db_query_bind("SELECT * FROM users WHERE id = $1", &data);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
