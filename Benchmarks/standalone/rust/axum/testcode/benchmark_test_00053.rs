// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;

pub async fn benchmark_test_00053() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = String::from_utf8_lossy(&hex::decode(&db_value).unwrap_or_default()).to_string();
    let parser = pulldown_cmark::Parser::new(&data);
    let mut md_rendered = String::new();
    pulldown_cmark::html::push_html(&mut md_rendered, parser);
    let processed = ammonia::clean(&md_rendered);
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
