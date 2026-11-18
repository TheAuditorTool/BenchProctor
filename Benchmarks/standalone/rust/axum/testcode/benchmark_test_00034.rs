// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00034(body: Bytes) -> impl IntoResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let data = xml_value.replace("\t", " ");
    reqwest::get(&data).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
