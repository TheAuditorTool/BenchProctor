// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;

pub async fn benchmark_test_00054(body: Bytes) -> impl IntoResponse {
    let graphql_var = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("variables").and_then(|vs| vs.get("input")).and_then(|i| i.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let data = match graphql_var.chars().next() { Some(_) => graphql_var.clone(), None => "default".to_string() };
    axum::response::Redirect::to(data.as_str()).into_response()
}
