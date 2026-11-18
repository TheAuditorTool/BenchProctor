// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00250")]
pub async fn benchmark_test_00250(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(referer_value.clone());
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
