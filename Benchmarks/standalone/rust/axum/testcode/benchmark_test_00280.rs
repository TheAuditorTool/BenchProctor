// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00280(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let multipart_value = {
        let mut _mv = String::new();
        if let Ok(Some(_field)) = multipart.next_field().await {
            _mv = _field.text().await.unwrap_or_default();
        }
        _mv
    };
    let _prefix: String = multipart_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => multipart_value.to_lowercase(),
        "f" => multipart_value.to_uppercase(),
        _ => multipart_value.trim().to_string(),
    };
    crate::shared::store_session("data", &data);
    Json(serde_json::json!({"count": 0})).into_response()
}
