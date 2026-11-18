// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00575")]
pub async fn benchmark_test_00575(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", referer_value).ok();
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = result.unwrap();
    let _ = value;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
