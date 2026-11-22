// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00187")]
pub async fn benchmark_test_00187(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let mut pending: std::collections::VecDeque<String> = xml_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    let _cookie = actix_web::cookie::Cookie::build("session", data.clone()).http_only(true).same_site(actix_web::cookie::SameSite::Strict).finish();
    return HttpResponse::Ok().cookie(_cookie).json(serde_json::json!({"stored": true}));
}
