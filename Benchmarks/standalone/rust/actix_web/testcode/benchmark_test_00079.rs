// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00079")]
pub async fn benchmark_test_00079(body: web::Bytes) -> HttpResponse {
    let graphql_var = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("variables").and_then(|vs| vs.get("input")).and_then(|i| i.as_str()).map(|s| s.to_string())).unwrap_or_default();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", graphql_var).ok();
    crate::shared::store_session("data", &data);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
