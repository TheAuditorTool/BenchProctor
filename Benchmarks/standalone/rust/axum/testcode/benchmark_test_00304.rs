// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00304(body: Bytes) -> impl IntoResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let data = serde_json::from_str::<serde_json::Value>(&json_value)
        .ok().and_then(|v| v["value"].as_str().map(|s| s.to_string())).unwrap_or_default();
    Command::new("sh").arg("-c").arg(format!("cat {}", data)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
