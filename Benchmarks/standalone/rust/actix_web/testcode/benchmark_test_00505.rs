// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00505")]
pub async fn benchmark_test_00505(body: web::Bytes) -> HttpResponse {
    let graphql_var = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("variables").and_then(|vs| vs.get("input")).and_then(|i| i.as_str()).map(|s| s.to_string())).unwrap_or_default();
    use md5::Digest;
    let _ = md5::Md5::digest(graphql_var.as_bytes());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
