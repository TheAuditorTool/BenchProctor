// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00151")]
pub async fn benchmark_test_00151(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let (payload, _origin) = (referer_value.clone(), "http");
    let data = payload;
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", data));
}
