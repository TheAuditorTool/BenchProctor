// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00273")]
pub async fn benchmark_test_00273() -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let data = env_value.replace("\t", " ");
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
