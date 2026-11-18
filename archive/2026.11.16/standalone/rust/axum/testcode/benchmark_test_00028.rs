// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::response::IntoResponse;
use std::collections::HashMap;

pub async fn benchmark_test_00028(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    let data = match user_id.chars().next() { Some(_) => user_id.clone(), None => "default".to_string() };
    let processed = html_escape::encode_text(&data).to_string();
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
