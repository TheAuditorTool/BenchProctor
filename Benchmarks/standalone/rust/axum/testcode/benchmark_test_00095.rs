// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00095() -> impl IntoResponse {
    let msg_value = crate::shared::queue_get_message("app-events");
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", msg_value).ok();
    let _q = format!("SELECT * FROM users WHERE id = '{}'", data);
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query(sqlx::AssertSqlSafe(_q)).execute(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
