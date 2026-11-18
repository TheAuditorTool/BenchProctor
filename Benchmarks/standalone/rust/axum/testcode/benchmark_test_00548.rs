// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00548(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Ok(Some(_field)) = multipart.next_field().await {
            if let Some(_f) = _field.file_name() { _fname = _f.to_string(); break; }
        }
        _fname
    };
    let mut data = String::new();
    for token in upload_name.split(',') { data = token.to_string(); }
    if let Ok(_pool) = sqlx::PgPool::connect("postgres://app:app@localhost/appdb").await {
        let _ = sqlx::query("SELECT id, name FROM users WHERE id = $1").bind(data.parse::<i32>().unwrap_or_default()).fetch_optional(&_pool).await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
