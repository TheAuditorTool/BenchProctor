// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00090")]
pub async fn benchmark_test_00090(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    struct FormData { payload: String }
    let data = FormData { payload: xml_value.clone() }.payload;
    HttpResponse::build(actix_web::http::StatusCode::SEE_OTHER).insert_header((actix_web::http::header::LOCATION, data.as_str())).finish()
}
