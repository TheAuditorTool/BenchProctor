// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00272")]
pub async fn benchmark_test_00272(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match auth_header.chars().next() { Some(_) => auth_header.clone(), None => "default".to_string() };
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", data));
}
