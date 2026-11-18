// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00086")]
pub async fn benchmark_test_00086(req: HttpRequest) -> HttpResponse {
    let origin_value = req.headers().get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = origin_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| origin_value.clone());
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
