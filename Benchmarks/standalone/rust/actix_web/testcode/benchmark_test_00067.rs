// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00067")]
pub async fn benchmark_test_00067() -> HttpResponse {
    let file_value = tokio::fs::read_to_string("/tmp/data").await.unwrap_or_default();
    let transform = |v: String| v.trim().to_string();
    let data = transform(file_value.clone());
    crate::shared::db_query(&format!("SELECT * FROM `{}`", data.replace('`', "")));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
