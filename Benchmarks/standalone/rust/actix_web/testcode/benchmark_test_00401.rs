// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00401")]
pub async fn benchmark_test_00401(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match referer_value.chars().next() { Some(_) => referer_value.clone(), None => "default".to_string() };
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", data));
}
