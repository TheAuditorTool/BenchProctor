// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00295(body: Bytes) -> impl IntoResponse {
    let graphql_var = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("variables").and_then(|vs| vs.get("input")).and_then(|i| i.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let _prefix: String = graphql_var.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => graphql_var.to_lowercase(),
        "f" => graphql_var.to_uppercase(),
        _ => graphql_var.trim().to_string(),
    };
    use sha2::Digest;
    let _ = sha2::Sha256::digest(data.as_bytes());
    Json(serde_json::json!({"count": 0})).into_response()
}
