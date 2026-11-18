// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00007")]
pub async fn benchmark_test_00007(req: HttpRequest) -> HttpResponse {
    let host_value = req.headers().get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = host_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    crate::shared::ldap_search(&format!("uid={}", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
