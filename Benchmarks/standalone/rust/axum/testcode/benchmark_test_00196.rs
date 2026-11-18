// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00196(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(raw_body.clone());
    crate::shared::set_cookie(&format!("session={}; Secure; HttpOnly; SameSite=Strict", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
