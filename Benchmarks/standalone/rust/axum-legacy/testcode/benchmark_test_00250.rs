// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00250(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Ok(Some(_field)) = multipart.next_field().await {
            if let Some(_f) = _field.file_name() { _fname = _f.to_string(); break; }
        }
        _fname
    };
    let mut data = String::new();
    for token in upload_name.split(',') { data = token.to_string(); }
    let _cookie = cookie::Cookie::build(("session", data.clone())).http_only(true).same_site(cookie::SameSite::Strict).build();
    return (axum::response::AppendHeaders([(axum::http::header::SET_COOKIE, _cookie.to_string())]), Json(serde_json::json!({"count": 0}))).into_response();
}
