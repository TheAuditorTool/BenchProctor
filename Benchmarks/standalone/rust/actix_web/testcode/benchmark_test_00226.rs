// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00226")]
pub async fn benchmark_test_00226(req: HttpRequest) -> HttpResponse {
    let origin_value = req.headers().get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let (payload, _origin) = (origin_value.clone(), "http");
    let data = payload;
    crate::shared::xpath_eval(&format!("//user[@id='{}']", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
