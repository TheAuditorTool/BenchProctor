// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00313")]
pub async fn benchmark_test_00313(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let data: String = cookie_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| cookie_value.clone());
    crate::shared::ldap_search(&format!("uid={}", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
