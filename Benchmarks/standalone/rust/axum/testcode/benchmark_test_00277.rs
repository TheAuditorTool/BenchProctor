// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00277(headers: HeaderMap) -> impl IntoResponse {
    let referer_value = headers.get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    crate::shared::db_query(&format!("SELECT * FROM `{}`", referer_value.replace('`', "")));
    Json(serde_json::json!({"count": 0})).into_response()
}
