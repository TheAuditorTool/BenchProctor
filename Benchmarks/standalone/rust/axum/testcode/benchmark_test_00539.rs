// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00539(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Ok(Some(_field)) = multipart.next_field().await {
            if let Some(_f) = _field.file_name() { _fname = _f.to_string(); break; }
        }
        _fname
    };
    let data = if upload_name.len() <= 4096 { upload_name.clone() } else { upload_name.chars().take(4096).collect() };
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query("SELECT * FROM users WHERE id = $1").bind(data.parse::<i32>().unwrap_or_default()).execute(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
