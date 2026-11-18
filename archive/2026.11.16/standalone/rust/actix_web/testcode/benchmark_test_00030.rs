// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00030")]
pub async fn benchmark_test_00030() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let mut pending: std::collections::VecDeque<String> = db_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    use rand::{Rng, SeedableRng};
    let _seed: u64 = data.bytes().fold(0u64, |a, b| a.wrapping_add(b as u64));
    let mut _rng = rand::rngs::StdRng::seed_from_u64(_seed);
    let _token: u64 = _rng.gen();
    crate::shared::store_session("csrf_token", &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
