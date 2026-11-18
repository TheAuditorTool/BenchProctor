// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00529")]
pub async fn benchmark_test_00529(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = auth_header.to_string();
    use rand::{Rng, SeedableRng};
    let _seed: u64 = data.bytes().fold(0u64, |a, b| a.wrapping_add(b as u64));
    let mut _rng = rand::rngs::StdRng::seed_from_u64(_seed);
    let _token: u64 = _rng.gen();
    crate::shared::store_session("csrf_token", &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
