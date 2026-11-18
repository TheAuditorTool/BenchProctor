// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00430() -> impl IntoResponse {
    let profile_value = crate::shared::db_fetch_one("SELECT bio FROM profiles LIMIT 1");
    let captured = profile_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let _q = format!("SELECT * FROM users WHERE id = '{}'", data);
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query(&_q).execute(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
