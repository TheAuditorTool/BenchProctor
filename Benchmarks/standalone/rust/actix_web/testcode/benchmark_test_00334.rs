// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00334")]
pub async fn benchmark_test_00334(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let captured = referer_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    crate::shared::ldap_search(&format!("uid={}", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
