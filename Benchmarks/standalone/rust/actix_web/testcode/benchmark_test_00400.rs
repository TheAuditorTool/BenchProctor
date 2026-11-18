// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00400")]
pub async fn benchmark_test_00400(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let mut pending: std::collections::VecDeque<String> = field_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    use rand::{Rng, SeedableRng};
    let _seed: u64 = data.bytes().fold(0u64, |a, b| a.wrapping_add(b as u64));
    let mut _rng = rand::rngs::StdRng::seed_from_u64(_seed);
    let _token: u64 = _rng.gen();
    crate::shared::store_session("csrf_token", &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
