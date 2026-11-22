// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;
use rand::rngs::OsRng;

pub async fn benchmark_test_00144(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let data = match path_value.chars().next() { Some(_) => path_value.clone(), None => "default".to_string() };
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    Json(serde_json::json!({"count": 0})).into_response()
}
