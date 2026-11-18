// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00288(headers: HeaderMap) -> impl IntoResponse {
    let cookie_value = headers.get("cookie").and_then(|v| v.to_str().ok()).and_then(|s| s.split(';').find(|c| c.trim_start().starts_with("session_token="))).map(|c| c.trim_start().trim_start_matches("session_token=").to_string()).unwrap_or_default();
    let transform = |v: String| v.trim().to_string();
    let data = transform(cookie_value.clone());
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query("SELECT id, name FROM users WHERE id = $1").bind(data.parse::<i32>().unwrap_or_default()).fetch_optional(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
