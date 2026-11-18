// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00056() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", comment_value).ok();
    crate::shared::db_query(&format!("SELECT * FROM `{}`", data.replace('`', "")));
    Json(serde_json::json!({"count": 0})).into_response()
}
