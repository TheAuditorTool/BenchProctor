// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00272")]
pub async fn benchmark_test_00272(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let captured = cookie_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", data));
}
