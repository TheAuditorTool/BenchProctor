// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::response::IntoResponse;
use std::collections::HashMap;

pub async fn benchmark_test_00083(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    let mut data = String::new();
    for token in user_id.split(',') { data = token.to_string(); }
    let processed = ammonia::clean(&data);
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
