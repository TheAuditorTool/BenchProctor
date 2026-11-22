// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00002")]
pub async fn benchmark_test_00002() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let data = if env_value.len() <= 4096 { env_value.clone() } else { env_value.chars().take(4096).collect() };
    HttpResponse::build(actix_web::http::StatusCode::SEE_OTHER).insert_header((actix_web::http::header::LOCATION, data.as_str())).finish()
}
