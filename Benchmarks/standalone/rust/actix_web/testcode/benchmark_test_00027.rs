// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00027")]
pub async fn benchmark_test_00027() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let captured = env_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let _bounded = data.parse::<i64>().unwrap_or(0).clamp(0, 2147483647);
    let processed = _bounded.to_string();
    let quantity: u32 = processed.parse().unwrap_or(0);
    let Some(total_cents) = quantity.checked_mul(1299) else { return HttpResponse::BadRequest().finish(); };
    crate::shared::db_exec_bind("INSERT INTO logs (data) VALUES ($1)", &total_cents.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
