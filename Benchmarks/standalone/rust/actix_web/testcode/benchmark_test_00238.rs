// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00238")]
pub async fn benchmark_test_00238(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let mut data = String::new();
    for token in cookie_value.split(',') { data = token.to_string(); }
    crate::shared::ldap_search(&format!("uid={}", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
