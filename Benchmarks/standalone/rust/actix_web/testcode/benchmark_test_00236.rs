// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00236")]
pub async fn benchmark_test_00236(body: web::Bytes) -> HttpResponse {
    let graphql_var = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("variables").and_then(|vs| vs.get("input")).and_then(|i| i.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let data = match graphql_var.chars().next() { Some(_) => graphql_var.clone(), None => "default".to_string() };
    crate::shared::ldap_search(&format!("uid={}", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
