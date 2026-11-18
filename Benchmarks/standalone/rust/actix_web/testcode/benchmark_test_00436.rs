// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00436")]
pub async fn benchmark_test_00436(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let mut data = String::new();
    for token in cookie_value.split(',') { data = token.to_string(); }
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
