// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00063")]
pub async fn benchmark_test_00063() -> HttpResponse {
    let profile_value = crate::shared::db_fetch_one("SELECT bio FROM profiles LIMIT 1");
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", profile_value)).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
