// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00206() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let captured = db_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    use sha1::Digest;
    let _ = sha1::Sha1::new().chain_update(data.as_bytes()).finalize();
    Json(serde_json::json!({"count": 0})).into_response()
}
