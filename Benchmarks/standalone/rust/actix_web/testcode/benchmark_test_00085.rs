// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use rand::rngs::SysRng;

#[actix_web::post("/benchmark_test_00085")]
pub async fn benchmark_test_00085(body: web::Bytes) -> HttpResponse {
    let graphql_var = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("variables").and_then(|vs| vs.get("input")).and_then(|i| i.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let transform = |v: String| v.trim().to_string();
    let data = transform(graphql_var.clone());
    use rand::Rng;
    let mut _rng: rand::rngs::StdRng = rand::make_rng();
    let _token = _rng.next_u64();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
