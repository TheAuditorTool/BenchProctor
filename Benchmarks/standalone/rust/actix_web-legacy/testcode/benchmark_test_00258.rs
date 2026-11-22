// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use base64::Engine;
use base64::engine::general_purpose;

#[actix_web::post("/benchmark_test_00258")]
pub async fn benchmark_test_00258(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&raw_body).unwrap_or_default()).to_string();
    return HttpResponse::Ok().insert_header((actix_web::http::header::SET_COOKIE, format!("session={}; HttpOnly; SameSite=Strict", urlencoding::encode(&data)))).json(serde_json::json!({"stored": true}));
}
