// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00516() -> impl IntoResponse {
    let redis_value = redis::Client::open("redis://cache:6379").ok().and_then(|client| client.get_connection().ok()).and_then(|mut conn| redis::cmd("GET").arg("user_data").query::<String>(&mut conn).ok()).unwrap_or_default();
    let _prefix: String = redis_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => redis_value.to_lowercase(),
        "f" => redis_value.to_uppercase(),
        _ => redis_value.trim().to_string(),
    };
    reqwest::get(&data).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
