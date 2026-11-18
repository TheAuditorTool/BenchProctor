// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;

pub async fn benchmark_test_00503(body: Bytes) -> impl IntoResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let data = match json_value.chars().next() { Some(_) => json_value.clone(), None => "default".to_string() };
    let parser = pulldown_cmark::Parser::new(&data);
    let mut md_rendered = String::new();
    pulldown_cmark::html::push_html(&mut md_rendered, parser);
    let processed = ammonia::clean(&md_rendered);
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
