// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00059")]
pub async fn benchmark_test_00059() -> HttpResponse {
    let api_value = crate::shared::fetch_url("https://api.partner.example.com/v1/records");
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", api_value).ok();
    crate::shared::db_query_bind_named("SELECT * FROM users WHERE id = :id", &data);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
