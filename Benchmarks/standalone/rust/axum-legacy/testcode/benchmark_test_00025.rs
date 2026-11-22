// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00025(headers: HeaderMap) -> impl IntoResponse {
    let header_value = headers.get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(header_value.clone());
    let _chunk = format!("<div>{}</div>", data);
    return ([("content-type", "text/html; charset=utf-8")], axum::body::Body::from_stream(futures_util::stream::once(async move { Ok::<_, std::convert::Infallible>(_chunk) }))).into_response();
}
