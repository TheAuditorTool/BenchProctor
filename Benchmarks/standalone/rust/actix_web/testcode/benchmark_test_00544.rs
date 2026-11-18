// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00544")]
pub async fn benchmark_test_00544(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = auth_header.replace("\t", " ");
    let base_dir = "/var/app/data";
    let full_path = tokio::fs::canonicalize(format!("{}/{}", base_dir, data)).await.unwrap_or_default();
    if !full_path.starts_with(base_dir) { return HttpResponse::Forbidden().finish(); }
    let checked_path = full_path.to_string_lossy().to_string();
    tokio::fs::remove_file(&checked_path).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
