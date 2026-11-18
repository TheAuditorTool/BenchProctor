// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;

pub async fn benchmark_test_00048(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    let data = String::from_utf8_lossy(&hex::decode(&user_id).unwrap_or_default()).to_string();
    reqwest::get(&data).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
