// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00082")]
pub async fn benchmark_test_00082() -> HttpResponse {
    let api_value = crate::shared::fetch_url("https://api.partner.example.com/v1/records");
    let captured = api_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let _coerced = data.parse::<i64>().unwrap_or(0);
    let processed = _coerced.to_string();
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = {}", processed));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
