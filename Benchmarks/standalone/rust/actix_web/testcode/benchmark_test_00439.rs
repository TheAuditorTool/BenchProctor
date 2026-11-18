// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00439")]
pub async fn benchmark_test_00439(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    struct FormData { payload: String }
    let data = FormData { payload: referer_value.clone() }.payload;
    crate::shared::ldap_search(&format!("uid={}", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
