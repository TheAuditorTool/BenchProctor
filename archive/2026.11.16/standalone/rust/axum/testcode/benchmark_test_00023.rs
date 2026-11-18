// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;

pub async fn benchmark_test_00023(body: Bytes) -> impl IntoResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", json_value).ok();
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
