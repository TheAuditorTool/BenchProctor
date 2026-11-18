// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00457")]
pub async fn benchmark_test_00457() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = String::from_utf8_lossy(&hex::decode(&db_value).unwrap_or_default()).to_string();
    let parser = pulldown_cmark::Parser::new(&data);
    let mut md_rendered = String::new();
    pulldown_cmark::html::push_html(&mut md_rendered, parser);
    let processed = ammonia::clean(&md_rendered);
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", processed));
}
