// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00182")]
pub async fn benchmark_test_00182(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut pending: std::collections::VecDeque<String> = header_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    let base = std::path::Path::new("/var/app/data");
    let candidate = tokio::fs::canonicalize(base.join(&data)).await.unwrap_or_default();
    if !candidate.starts_with(base) { return HttpResponse::Forbidden().finish(); }
    let checked_path = candidate.to_string_lossy().to_string();
    tokio::fs::remove_file(&checked_path).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
