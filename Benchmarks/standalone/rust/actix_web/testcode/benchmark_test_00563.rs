// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use rand::rngs::OsRng;

#[actix_web::post("/benchmark_test_00563")]
pub async fn benchmark_test_00563(body: web::Bytes) -> HttpResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let data = if json_value.len() <= 4096 { json_value.clone() } else { json_value.chars().take(4096).collect() };
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
