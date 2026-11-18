// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00203")]
pub async fn benchmark_test_00203(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", auth_header));
}
