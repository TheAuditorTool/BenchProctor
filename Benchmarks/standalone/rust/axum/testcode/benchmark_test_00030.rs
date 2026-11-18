// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00030() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = if db_value.len() <= 4096 { db_value.clone() } else { db_value.chars().take(4096).collect() };
    let _q = format!("SELECT * FROM users WHERE id = '{}'", data);
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query(&_q).execute(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
