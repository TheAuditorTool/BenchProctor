// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00423(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let (payload, _origin) = (raw_body.clone(), "http");
    let data = payload;
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", data)).await;
    Json(serde_json::json!({"count": 0})).into_response()
}
