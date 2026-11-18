// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00353")]
pub async fn benchmark_test_00353(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = raw_body.to_string();
    tokio::fs::remove_file(format!("/var/app/data/{}", data)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
