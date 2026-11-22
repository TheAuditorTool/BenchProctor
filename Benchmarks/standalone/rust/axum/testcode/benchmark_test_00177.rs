// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00177(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let multipart_value = {
        let mut _mv = String::new();
        if let Ok(Some(_field)) = multipart.next_field().await {
            _mv = _field.text().await.unwrap_or_default();
        }
        _mv
    };
    let data: String = multipart_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| multipart_value.clone());
    if let Ok(_target) = reqwest::Url::parse(&data) {
        let _request = reqwest::Request::new(reqwest::Method::GET, _target);
        let _client = reqwest::Client::new();
        _client.execute(_request).await.ok();
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
