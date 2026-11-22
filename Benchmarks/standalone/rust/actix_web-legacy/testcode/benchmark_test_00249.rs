// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00249")]
pub async fn benchmark_test_00249(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(xml_value.clone());
    let base = std::path::Path::new("/var/app/data");
    let candidate = tokio::fs::canonicalize(base.join(&data)).await.unwrap_or_default();
    if !candidate.starts_with(base) { return HttpResponse::Forbidden().finish(); }
    let checked_path = candidate.to_string_lossy().to_string();
    let _ = tokio::fs::read_to_string(&checked_path).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
