// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;

pub async fn benchmark_test_00573() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let captured = db_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
