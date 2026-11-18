// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;
use rand::rngs::OsRng;

pub async fn benchmark_test_00382() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let captured = db_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    Json(serde_json::json!({"count": 0})).into_response()
}
