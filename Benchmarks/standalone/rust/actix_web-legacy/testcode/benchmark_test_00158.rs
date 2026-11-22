// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00158")]
pub async fn benchmark_test_00158(req: HttpRequest) -> HttpResponse {
    let forwarded_ip = req.headers().get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let _prefix: String = forwarded_ip.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => forwarded_ip.to_lowercase(),
        "f" => forwarded_ip.to_uppercase(),
        _ => forwarded_ip.trim().to_string(),
    };
    if let Ok(mut _app_context) = crate::shared::APP_CONTEXT.write() {
        _app_context.insert("partner_tier".to_string(), data.clone());
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
