// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00018(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let multipart_value = {
        let mut _mv = String::new();
        if let Ok(Some(_field)) = multipart.next_field().await {
            _mv = _field.text().await.unwrap_or_default();
        }
        _mv
    };
    let captured = multipart_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    crate::shared::ldap_search(&format!("uid={}", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
