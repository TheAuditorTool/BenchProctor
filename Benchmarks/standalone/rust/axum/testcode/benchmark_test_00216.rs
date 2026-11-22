// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;

pub async fn benchmark_test_00216(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    let (payload, _origin) = (user_id.clone(), "http");
    let data = payload;
    use sha2::Digest;
    let mut _hasher = sha2::Sha256::new();
    _hasher.update(data.as_bytes());
    let _ = _hasher.finalize();
    Json(serde_json::json!({"count": 0})).into_response()
}
