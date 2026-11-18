// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;

pub async fn benchmark_test_00023(body: Bytes) -> impl IntoResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = raw_body.replace("\t", " ");
    let processed = ammonia::clean(&data);
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
