// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00593(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Ok(Some(_field)) = multipart.next_field().await {
            if let Some(_f) = _field.file_name() { _fname = _f.to_string(); break; }
        }
        _fname
    };
    let _prefix: String = upload_name.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => upload_name.to_lowercase(),
        "f" => upload_name.to_uppercase(),
        _ => upload_name.trim().to_string(),
    };
    crate::shared::set_cookie(&format!("session={}; Secure; HttpOnly; SameSite=Strict", data));
    Json(serde_json::json!({"count": 0})).into_response()
}
