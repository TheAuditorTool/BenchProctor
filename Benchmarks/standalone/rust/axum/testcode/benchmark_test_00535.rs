// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00535() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = match comment_value.chars().next() { Some(_) => comment_value.clone(), None => "default".to_string() };
    crate::shared::ldap_search(&format!("uid={}", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
