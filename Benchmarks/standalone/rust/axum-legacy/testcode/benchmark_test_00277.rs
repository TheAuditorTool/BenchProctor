// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00277() -> impl IntoResponse {
    let upload_name = crate::shared::uploaded_filename();
    let data = upload_name.to_string();
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", data)).await;
    Json(serde_json::json!({"count": 0})).into_response()
}
