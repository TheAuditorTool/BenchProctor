// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00251() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    use sha2::Digest;
    let _ = sha2::Sha256::digest(comment_value.as_bytes());
    Json(serde_json::json!({"count": 0})).into_response()
}
