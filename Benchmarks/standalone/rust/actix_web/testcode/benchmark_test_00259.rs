// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00259")]
pub async fn benchmark_test_00259(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", cookie_value).ok();
    let base = std::path::Path::new("/var/app/data");
    let candidate = tokio::fs::canonicalize(base.join(&data)).await.unwrap_or_default();
    if !candidate.starts_with(base) { return HttpResponse::Forbidden().finish(); }
    let checked_path = candidate.to_string_lossy().to_string();
    let _ = tokio::fs::read_to_string(&checked_path).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
