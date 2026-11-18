// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00077")]
pub async fn benchmark_test_00077(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let data = cookie_value.to_string();
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = match result { Some(v) => v, None => return HttpResponse::NotFound().finish() };
    let _ = value;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
