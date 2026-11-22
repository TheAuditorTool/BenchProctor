// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00289")]
pub async fn benchmark_test_00289(req: HttpRequest) -> HttpResponse {
    let origin_value = req.headers().get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = if origin_value.len() <= 4096 { origin_value.clone() } else { origin_value.chars().take(4096).collect() };
    let checked_path = format!("/var/app/data/{}", std::path::Path::new(&data).file_name().and_then(|n| n.to_str()).unwrap_or(""));
    tokio::fs::remove_file(&checked_path).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
