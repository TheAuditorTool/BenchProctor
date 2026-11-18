// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00072(body: Bytes) -> impl IntoResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let data = serde_json::from_str::<serde_json::Value>(&json_value)
        .ok().and_then(|v| v["value"].as_str().map(|s| s.to_string())).unwrap_or_default();
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query("SELECT * FROM users WHERE id = $1").bind(data.parse::<i32>().unwrap_or_default()).execute(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
