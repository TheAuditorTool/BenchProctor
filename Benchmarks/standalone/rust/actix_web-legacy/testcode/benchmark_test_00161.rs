// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00161")]
pub async fn benchmark_test_00161(req: HttpRequest) -> HttpResponse {
    let host_value = req.headers().get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = if host_value.len() <= 4096 { host_value.clone() } else { host_value.chars().take(4096).collect() };
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
