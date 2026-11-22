// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::http::StatusCode;
use axum::response::IntoResponse;

pub async fn benchmark_test_00233(body: Bytes) -> impl IntoResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    struct FormData { payload: String }
    let data = FormData { payload: xml_value.clone() }.payload;
    (StatusCode::FOUND, [(axum::http::header::LOCATION, data.clone())]).into_response()
}
