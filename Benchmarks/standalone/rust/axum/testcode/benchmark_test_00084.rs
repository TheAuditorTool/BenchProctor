// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00084(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Ok(Some(_field)) = multipart.next_field().await {
            if let Some(_f) = _field.file_name() { _fname = _f.to_string(); break; }
        }
        _fname
    };
    crate::shared::set_cookie(&format!("session={}; Secure; HttpOnly; SameSite=Strict", upload_name));
    Json(serde_json::json!({"count": 0})).into_response()
}
