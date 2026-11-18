// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00498")]
pub async fn benchmark_test_00498(req: HttpRequest) -> HttpResponse {
    let host_value = req.headers().get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(host_value.clone());
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", data)).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
