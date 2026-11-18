// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00439(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Ok(Some(_field)) = multipart.next_field().await {
            if let Some(_f) = _field.file_name() { _fname = _f.to_string(); break; }
        }
        _fname
    };
    let mut pending: std::collections::VecDeque<String> = upload_name.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = result.unwrap();
    let _ = value;
    Json(serde_json::json!({"count": 0})).into_response()
}
