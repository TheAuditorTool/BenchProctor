// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00045")]
pub async fn benchmark_test_00045(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut pending: std::collections::VecDeque<String> = referer_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    let _coerced = matches!(data.to_lowercase().as_str(), "true" | "1" | "yes" | "on");
    let processed = _coerced.to_string();
    crate::shared::xpath_eval(&format!("//user[@id='{}']", processed));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
