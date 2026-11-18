// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00368")]
pub async fn benchmark_test_00368() -> HttpResponse {
    let api_value = crate::shared::fetch_url("https://api.partner.example.com/v1/records");
    let data = api_value.to_string();
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = '{}'", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
