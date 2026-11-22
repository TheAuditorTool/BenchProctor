// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00059(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Ok(Some(_field)) = multipart.next_field().await {
            if let Some(_f) = _field.file_name() { _fname = _f.to_string(); break; }
        }
        _fname
    };
    let (payload, _origin) = (upload_name.clone(), "http");
    let data = payload;
    let Some(at) = data.find('@') else { return (StatusCode::BAD_REQUEST, "").into_response(); };
    let mail_domain = &data[at + 1..];
    let _ = mail_domain;
    Json(serde_json::json!({"count": 0})).into_response()
}
