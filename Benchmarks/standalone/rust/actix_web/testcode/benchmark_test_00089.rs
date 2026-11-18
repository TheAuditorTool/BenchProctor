// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00089")]
pub async fn benchmark_test_00089(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = auth_header.replace("\t", " ");
    if !["config.json", "index.html", "readme.md"].contains(&data.as_str()) { return HttpResponse::Forbidden().finish(); }
    let checked_path = format!("/var/app/data/{}", data);
    tokio::fs::write(&checked_path, "data").await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
