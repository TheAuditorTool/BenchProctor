// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00017")]
pub async fn benchmark_test_00017(body: web::Bytes) -> HttpResponse {
    let graphql_var = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("variables").and_then(|vs| vs.get("input")).and_then(|i| i.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let (payload, _origin) = (graphql_var.clone(), "http");
    let data = payload;
    let rows: u32 = data.parse().unwrap_or(0);
    let _records: Vec<u8> = Vec::with_capacity((rows * 512) as usize);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
