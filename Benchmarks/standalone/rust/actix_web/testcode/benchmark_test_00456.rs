// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00456")]
pub async fn benchmark_test_00456(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", auth_header).ok();
    let base_dir = "/var/app/data";
    let full_path = tokio::fs::canonicalize(format!("{}/{}", base_dir, data)).await.unwrap_or_default();
    if !full_path.starts_with(base_dir) { return HttpResponse::Forbidden().finish(); }
    let checked_path = full_path.to_string_lossy().to_string();
    let _ = tokio::fs::read_to_string(&checked_path).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
