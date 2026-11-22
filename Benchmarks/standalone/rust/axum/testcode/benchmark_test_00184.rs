// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00184() -> impl IntoResponse {
    let api_value = crate::shared::fetch_url("https://api.partner.example.com/v1/records");
    let mut data = String::new();
    for token in api_value.split(',') { data = token.to_string(); }
    let _q = format!("SELECT * FROM users WHERE id = '{}'", data);
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query(sqlx::AssertSqlSafe(_q)).execute(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
