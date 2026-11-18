// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00003")]
pub async fn benchmark_test_00003(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut data = String::new();
    for token in referer_value.split(',') { data = token.to_string(); }
    let processed = ammonia::clean(&data);
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", processed));
}
