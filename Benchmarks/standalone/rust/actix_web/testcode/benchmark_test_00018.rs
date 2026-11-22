// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00018")]
pub async fn benchmark_test_00018(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let data = match xml_value.chars().next() { Some(_) => xml_value.clone(), None => "default".to_string() };
    if let Ok(mut _app_context) = crate::shared::APP_CONTEXT.write() {
        _app_context.insert("partner_tier".to_string(), data.clone());
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
