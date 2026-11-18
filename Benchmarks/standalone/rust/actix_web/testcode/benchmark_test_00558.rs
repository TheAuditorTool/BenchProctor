// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00558")]
pub async fn benchmark_test_00558(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let data = if xml_value.len() <= 4096 { xml_value.clone() } else { xml_value.chars().take(4096).collect() };
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = result.unwrap();
    let _ = value;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
