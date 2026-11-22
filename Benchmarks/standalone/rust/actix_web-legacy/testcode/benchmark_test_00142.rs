// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00142")]
pub async fn benchmark_test_00142(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", auth_header).ok();
    return HttpResponse::Ok().insert_header((actix_web::http::header::SET_COOKIE, format!("session={}; Secure; HttpOnly; SameSite=Strict", urlencoding::encode(&data)))).json(serde_json::json!({"stored": true}));
}
