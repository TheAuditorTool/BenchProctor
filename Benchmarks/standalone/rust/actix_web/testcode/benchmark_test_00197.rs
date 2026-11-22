// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00197")]
pub async fn benchmark_test_00197(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", ua_value).ok();
    if let Ok(mut _app_context) = crate::shared::APP_CONTEXT.write() {
        _app_context.insert("partner_tier".to_string(), data.clone());
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
