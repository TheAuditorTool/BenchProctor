// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00455(body: Bytes) -> impl IntoResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    struct FormData { payload: String }
    let data = FormData { payload: xml_value.clone() }.payload;
    let _coerced = data.parse::<f64>().unwrap_or(0.0);
    let processed = _coerced.to_string();
    crate::shared::store_session("data", &processed);
    Json(serde_json::json!({"count": 0})).into_response()
}
