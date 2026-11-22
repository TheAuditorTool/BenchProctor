// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::response::IntoResponse;
use std::collections::HashMap;

pub async fn benchmark_test_00201(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    let data = match user_id.chars().next() { Some(_) => user_id.clone(), None => "default".to_string() };
    axum::response::Redirect::temporary(data.as_str()).into_response()
}
