// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::response::IntoResponse;
use std::collections::HashMap;

pub async fn benchmark_test_00195(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    let captured = user_id.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
