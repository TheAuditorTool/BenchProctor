// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00040")]
pub async fn benchmark_test_00040() -> HttpResponse {
    let api_value = crate::shared::fetch_url("https://api.partner.example.com/v1/records");
    let _prefix: String = api_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => api_value.to_lowercase(),
        "f" => api_value.to_uppercase(),
        _ => api_value.trim().to_string(),
    };
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
