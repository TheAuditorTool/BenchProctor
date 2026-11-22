// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00103(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let captured = raw_body.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let _q = format!("SELECT * FROM users WHERE id = '{}'", data);
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query(sqlx::AssertSqlSafe(_q)).execute(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
