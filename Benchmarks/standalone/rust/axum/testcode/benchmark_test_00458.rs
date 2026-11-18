// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;
use rand::rngs::OsRng;

pub async fn benchmark_test_00458(body: Bytes) -> impl IntoResponse {
    let graphql_var = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("variables").and_then(|vs| vs.get("input")).and_then(|i| i.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let data = serde_json::from_str::<serde_json::Value>(&graphql_var)
        .ok().and_then(|v| v["value"].as_str().map(|s| s.to_string())).unwrap_or_default();
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    Json(serde_json::json!({"count": 0})).into_response()
}
