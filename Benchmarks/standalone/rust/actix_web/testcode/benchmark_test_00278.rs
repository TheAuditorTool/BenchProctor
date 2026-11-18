// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00278")]
pub async fn benchmark_test_00278(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = if auth_header.len() <= 4096 { auth_header.clone() } else { auth_header.chars().take(4096).collect() };
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
