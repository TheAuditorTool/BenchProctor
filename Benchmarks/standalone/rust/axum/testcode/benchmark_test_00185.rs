// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00185() -> impl IntoResponse {
    let api_value = crate::shared::fetch_url("https://api.partner.example.com/v1/records");
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", api_value).ok();
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query("SELECT id, name FROM users WHERE id = $1").bind(data.parse::<i32>().unwrap_or_default()).fetch_optional(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
