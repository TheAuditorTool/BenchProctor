// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00219(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let multipart_value = {
        let mut _mv = String::new();
        if let Ok(Some(_field)) = multipart.next_field().await {
            _mv = _field.text().await.unwrap_or_default();
        }
        _mv
    };
    let mut pending: std::collections::VecDeque<String> = multipart_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    crate::shared::store_session("data", &data);
    Json(serde_json::json!({"count": 0})).into_response()
}
