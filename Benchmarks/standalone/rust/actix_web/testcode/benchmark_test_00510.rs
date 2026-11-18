// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00510")]
pub async fn benchmark_test_00510(req: HttpRequest) -> HttpResponse {
    let forwarded_ip = req.headers().get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = if forwarded_ip.len() <= 4096 { forwarded_ip.clone() } else { forwarded_ip.chars().take(4096).collect() };
    let _coerced = data.parse::<f64>().unwrap_or(0.0);
    let processed = _coerced.to_string();
    crate::shared::xpath_eval(&format!("//user[@id='{}']", processed));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
