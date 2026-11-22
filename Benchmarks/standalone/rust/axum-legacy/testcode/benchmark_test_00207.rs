// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;

pub async fn benchmark_test_00207(headers: HeaderMap) -> impl IntoResponse {
    let auth_header = headers.get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(auth_header.clone());
    let processed = ammonia::clean(&data);
    let _chunk = format!("<div>{}</div>", processed);
    return ([("content-type", "text/html; charset=utf-8")], axum::body::Body::from_stream(futures_util::stream::once(async move { Ok::<_, std::convert::Infallible>(_chunk) }))).into_response();
}
