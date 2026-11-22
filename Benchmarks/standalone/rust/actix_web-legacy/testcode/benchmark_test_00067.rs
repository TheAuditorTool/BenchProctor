// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00067")]
pub async fn benchmark_test_00067(req: HttpRequest) -> HttpResponse {
    let origin_value = req.headers().get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let captured = origin_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
