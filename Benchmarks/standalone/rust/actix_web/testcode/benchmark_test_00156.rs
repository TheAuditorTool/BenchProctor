// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00156")]
pub async fn benchmark_test_00156(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let captured = ua_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let at = data.find('@').unwrap();
    let mail_domain = &data[at + 1..];
    let _ = mail_domain;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
