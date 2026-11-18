// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00473(body: Bytes) -> impl IntoResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let data = if xml_value.len() <= 4096 { xml_value.clone() } else { xml_value.chars().take(4096).collect() };
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = result.unwrap();
    let _ = value;
    Json(serde_json::json!({"count": 0})).into_response()
}
