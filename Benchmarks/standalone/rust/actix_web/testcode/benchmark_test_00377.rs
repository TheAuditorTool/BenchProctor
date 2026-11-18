// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00377")]
pub async fn benchmark_test_00377(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match auth_header.chars().next() { Some(_) => auth_header.clone(), None => "default".to_string() };
    reqwest::get(&data).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
