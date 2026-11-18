// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00370")]
pub async fn benchmark_test_00370(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let (payload, _origin) = (raw_body.clone(), "http");
    let data = payload;
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", data)).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
