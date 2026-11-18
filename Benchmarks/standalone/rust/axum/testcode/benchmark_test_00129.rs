// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00129() -> impl IntoResponse {
    let config_value = tokio::fs::read_to_string("/etc/app/config.json").await.unwrap_or_default();
    let captured = config_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let _q = format!("SELECT * FROM users WHERE id = '{}'", data);
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query(&_q).execute(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
