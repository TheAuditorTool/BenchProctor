// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;

pub async fn benchmark_test_00178(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    use md5::Digest;
    let _ = md5::Md5::digest(user_id.as_bytes());
    Json(serde_json::json!({"count": 0})).into_response()
}
