// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00117(body: Bytes) -> impl IntoResponse {
    let graphql_var = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("variables").and_then(|vs| vs.get("input")).and_then(|i| i.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let (payload, _origin) = (graphql_var.clone(), "http");
    let data = payload;
    use sha2::Digest;
    let _ = sha2::Sha256::new().chain_update(data.as_bytes()).finalize();
    Json(serde_json::json!({"count": 0})).into_response()
}
