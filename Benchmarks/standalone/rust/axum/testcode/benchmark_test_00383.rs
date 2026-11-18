// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use base64::Engine;
use base64::engine::general_purpose;

pub async fn benchmark_test_00383(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&raw_body).unwrap_or_default()).to_string();
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
