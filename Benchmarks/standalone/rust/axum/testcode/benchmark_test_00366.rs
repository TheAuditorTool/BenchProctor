// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;

pub async fn benchmark_test_00366(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", user_id)).await;
    Json(serde_json::json!({"count": 0})).into_response()
}
