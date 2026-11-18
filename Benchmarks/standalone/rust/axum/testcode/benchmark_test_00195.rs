// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;

pub async fn benchmark_test_00195() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let captured = comment_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    axum::response::Redirect::to(data.as_str()).into_response()
}
