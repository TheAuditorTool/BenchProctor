// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;

pub async fn benchmark_test_00518(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(user_id.clone());
    let _coerced = data.parse::<i64>().unwrap_or(0);
    let processed = _coerced.to_string();
    let _q = format!("SELECT * FROM users WHERE id = {}", processed);
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query(&_q).execute(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
