// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00513")]
pub async fn benchmark_test_00513(body: web::Bytes) -> HttpResponse {
    let graphql_var = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("variables").and_then(|vs| vs.get("input")).and_then(|i| i.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let (payload, _origin) = (graphql_var.clone(), "http");
    let data = payload;
    if !["config.json", "index.html", "readme.md"].contains(&data.as_str()) { return HttpResponse::Forbidden().finish(); }
    let checked_path = format!("/var/app/data/{}", data);
    tokio::fs::remove_file(&checked_path).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
