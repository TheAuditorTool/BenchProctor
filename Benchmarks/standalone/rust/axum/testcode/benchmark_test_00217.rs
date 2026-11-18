// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;

pub async fn benchmark_test_00217(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    let transform = |v: String| v.trim().to_string();
    let data = transform(user_id.clone());
    use md5::Digest;
    let _ = md5::Md5::digest(data.as_bytes());
    Json(serde_json::json!({"count": 0})).into_response()
}
