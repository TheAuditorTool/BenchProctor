// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00014() -> impl IntoResponse {
    let msg_value = crate::shared::queue_get_message("app-events");
    let data = msg_value.replace("\t", " ");
    reqwest::get(&data).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
