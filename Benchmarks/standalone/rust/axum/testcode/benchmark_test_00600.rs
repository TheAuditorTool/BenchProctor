// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::response::IntoResponse;
use std::collections::HashMap;

pub async fn benchmark_test_00600(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    let mut data = String::new();
    for token in user_id.split(',') { data = token.to_string(); }
    axum::response::Redirect::to(data.as_str()).into_response()
}
