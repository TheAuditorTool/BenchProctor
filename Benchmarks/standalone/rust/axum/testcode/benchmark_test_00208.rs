// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00208() -> impl IntoResponse {
    let api_value = crate::shared::fetch_url("https://api.partner.example.com/v1/records");
    let data = if api_value.len() <= 4096 { api_value.clone() } else { api_value.chars().take(4096).collect() };
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query("SELECT * FROM users WHERE id = $1").bind(data.parse::<i32>().unwrap_or_default()).execute(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
