// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00449")]
pub async fn benchmark_test_00449(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let data = String::from_utf8_lossy(xml_value.as_bytes()).to_string();
    crate::shared::ldap_search(&format!("uid={}", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
