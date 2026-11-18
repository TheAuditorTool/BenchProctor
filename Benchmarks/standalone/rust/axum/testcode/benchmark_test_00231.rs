// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00231(headers: HeaderMap) -> impl IntoResponse {
    let origin_value = headers.get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = origin_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| origin_value.clone());
    use rand::{Rng, SeedableRng};
    let _seed: u64 = data.bytes().fold(0u64, |a, b| a.wrapping_add(b as u64));
    let mut _rng = rand::rngs::StdRng::seed_from_u64(_seed);
    let _token: u64 = _rng.gen();
    crate::shared::store_session("csrf_token", &_token.to_string());
    Json(serde_json::json!({"count": 0})).into_response()
}
