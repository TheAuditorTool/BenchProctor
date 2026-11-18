// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00459(body: Bytes) -> impl IntoResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let (payload, _origin) = (xml_value.clone(), "http");
    let data = payload;
    crate::shared::ldap_search(&format!("uid={}", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
