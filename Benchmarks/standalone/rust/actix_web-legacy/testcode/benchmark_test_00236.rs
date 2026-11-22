// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00236")]
pub async fn benchmark_test_00236(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = referer_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| referer_value.clone());
    HttpResponse::build(actix_web::http::StatusCode::SEE_OTHER).insert_header((actix_web::http::header::LOCATION, data.as_str())).finish()
}
