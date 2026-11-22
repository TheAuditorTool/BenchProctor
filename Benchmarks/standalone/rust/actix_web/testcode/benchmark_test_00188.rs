// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00188")]
pub async fn benchmark_test_00188() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(db_value.clone());
    tokio::fs::write(format!("/var/app/data/{}", data), "data").await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
