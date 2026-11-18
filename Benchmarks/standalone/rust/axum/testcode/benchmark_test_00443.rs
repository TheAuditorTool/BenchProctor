// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00443(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let multipart_value = {
        let mut _mv = String::new();
        if let Ok(Some(_field)) = multipart.next_field().await {
            _mv = _field.text().await.unwrap_or_default();
        }
        _mv
    };
    let (payload, _origin) = (multipart_value.clone(), "http");
    let data = payload;
    use sha2::Digest;
    let _ = sha2::Sha256::digest(data.as_bytes());
    Json(serde_json::json!({"count": 0})).into_response()
}
