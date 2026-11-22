// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00243(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Ok(Some(_field)) = multipart.next_field().await {
            if let Some(_f) = _field.file_name() { _fname = _f.to_string(); break; }
        }
        _fname
    };
    let data = if upload_name.len() <= 4096 { upload_name.clone() } else { upload_name.chars().take(4096).collect() };
    use sha1::Digest;
    let _ = sha1::Sha1::new().chain_update(data.as_bytes()).finalize();
    Json(serde_json::json!({"count": 0})).into_response()
}
