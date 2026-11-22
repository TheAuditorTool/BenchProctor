// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00167")]
pub async fn benchmark_test_00167(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = referer_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    tokio::fs::write(format!("/var/app/data/{}", data), "data").await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
