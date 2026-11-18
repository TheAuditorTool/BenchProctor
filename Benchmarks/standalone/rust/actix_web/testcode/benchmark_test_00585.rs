// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00585")]
pub async fn benchmark_test_00585(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let data = cookie_value.to_string();
    let parser = pulldown_cmark::Parser::new(&data);
    let mut md_rendered = String::new();
    pulldown_cmark::html::push_html(&mut md_rendered, parser);
    let processed = ammonia::clean(&md_rendered);
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", processed));
}
