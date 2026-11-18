// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00227")]
pub async fn benchmark_test_00227(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = header_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| header_value.clone());
    crate::shared::xpath_eval(&format!("//user[@id='{}']", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
