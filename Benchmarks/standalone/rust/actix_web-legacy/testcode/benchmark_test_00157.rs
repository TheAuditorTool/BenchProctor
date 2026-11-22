// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00157")]
pub async fn benchmark_test_00157(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let data = xml_value.replace("\t", " ");
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
