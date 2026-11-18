// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00116(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = match raw_body.chars().next() { Some(_) => raw_body.clone(), None => "default".to_string() };
    crate::shared::xpath_eval(&format!("//user[@id='{}']", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
