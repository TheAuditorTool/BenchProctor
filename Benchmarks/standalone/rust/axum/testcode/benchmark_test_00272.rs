// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;

pub async fn benchmark_test_00272() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let transform = |v: String| v.trim().to_string();
    let data = transform(comment_value.clone());
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
