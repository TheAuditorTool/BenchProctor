// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;
use rand::rngs::OsRng;

pub async fn benchmark_test_00009() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let _prefix: String = comment_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => comment_value.to_lowercase(),
        "f" => comment_value.to_uppercase(),
        _ => comment_value.trim().to_string(),
    };
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    Json(serde_json::json!({"count": 0})).into_response()
}
