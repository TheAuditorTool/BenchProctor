// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00555() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = if comment_value.len() <= 4096 { comment_value.clone() } else { comment_value.chars().take(4096).collect() };
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query("SELECT * FROM users WHERE id = $1").bind(data.parse::<i32>().unwrap_or_default()).execute(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
