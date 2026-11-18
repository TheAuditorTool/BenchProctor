// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00262")]
pub async fn benchmark_test_00262(req: HttpRequest) -> HttpResponse {
    let origin_value = req.headers().get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(origin_value.clone());
    tokio::fs::write(format!("/var/app/data/{}", data), "data").await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
