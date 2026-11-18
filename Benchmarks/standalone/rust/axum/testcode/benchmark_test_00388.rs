// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00388(body: Bytes) -> impl IntoResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    crate::shared::set_cookie(&format!("session={}; HttpOnly; SameSite=Strict", json_value));
    Json(serde_json::json!({"count": 0})).into_response()
}
