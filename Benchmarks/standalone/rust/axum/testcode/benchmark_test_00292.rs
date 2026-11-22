// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00292(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Ok(Some(_field)) = multipart.next_field().await {
            if let Some(_f) = _field.file_name() { _fname = _f.to_string(); break; }
        }
        _fname
    };
    let data: String = upload_name.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| upload_name.clone());
    reqwest::get(&data).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
