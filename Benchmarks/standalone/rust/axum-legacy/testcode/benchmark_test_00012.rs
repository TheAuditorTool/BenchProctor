// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00012() -> impl IntoResponse {
    let api_value = crate::shared::fetch_url("https://api.partner.example.com/v1/records");
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(api_value.clone());
    reqwest::get(&data).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
