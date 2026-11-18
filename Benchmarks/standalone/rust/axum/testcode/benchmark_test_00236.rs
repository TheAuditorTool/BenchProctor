// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00236() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let mut data = String::new();
    for token in comment_value.split(',') { data = token.to_string(); }
    crate::shared::xpath_eval(&format!("//user[@id='{}']", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
