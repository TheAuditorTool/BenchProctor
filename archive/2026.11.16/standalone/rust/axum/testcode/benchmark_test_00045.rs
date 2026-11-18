// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00045() -> impl IntoResponse {
    let api_value = crate::shared::fetch_url("https://api.partner.example.com/v1/records");
    let captured = api_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let _coerced = data.parse::<i64>().unwrap_or(0);
    let processed = _coerced.to_string();
    let _q = format!("SELECT * FROM users WHERE id = {}", processed);
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query(&_q).execute(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
