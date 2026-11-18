// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00031")]
pub async fn benchmark_test_00031(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = raw_body.replace("\t", " ");
    let processed = ammonia::clean(&data);
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", processed));
}
