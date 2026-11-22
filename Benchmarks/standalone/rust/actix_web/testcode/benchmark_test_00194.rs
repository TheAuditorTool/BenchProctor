// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00194")]
pub async fn benchmark_test_00194(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let mut data = String::new();
    for token in raw_body.split(',') { data = token.to_string(); }
    return HttpResponse::Ok().insert_header((actix_web::http::header::SET_COOKIE, format!("session={}; Secure; HttpOnly; SameSite=Strict", urlencoding::encode(&data)))).json(serde_json::json!({"stored": true}));
}
