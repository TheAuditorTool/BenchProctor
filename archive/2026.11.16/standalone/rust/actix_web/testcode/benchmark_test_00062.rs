// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00062")]
pub async fn benchmark_test_00062() -> HttpResponse {
    let api_value = crate::shared::fetch_url("https://api.partner.example.com/v1/records");
    let data = api_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
