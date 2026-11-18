// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;

pub async fn benchmark_test_00039(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", user_id).ok();
    crate::shared::xpath_eval(&format!("//user[@id='{}']", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
