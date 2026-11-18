// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00348")]
pub async fn benchmark_test_00348(req: HttpRequest) -> HttpResponse {
    let host_value = req.headers().get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut data = String::new();
    for token in host_value.split(',') { data = token.to_string(); }
    tokio::fs::remove_file(format!("/var/app/data/{}", data)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
