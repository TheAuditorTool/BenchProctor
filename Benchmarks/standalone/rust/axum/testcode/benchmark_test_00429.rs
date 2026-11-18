// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00429() -> impl IntoResponse {
    let file_value = tokio::fs::read_to_string("/tmp/data").await.unwrap_or_default();
    let mut data = String::new();
    for token in file_value.split(',') { data = token.to_string(); }
    let _q = format!("SELECT * FROM users WHERE id = '{}'", data);
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query(&_q).execute(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
