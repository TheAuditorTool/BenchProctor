// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00160")]
pub async fn benchmark_test_00160(req: HttpRequest) -> HttpResponse {
    let forwarded_ip = req.headers().get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = forwarded_ip.replace("\t", " ");
    crate::shared::set_cookie(&format!("session={}; Secure; HttpOnly; SameSite=Strict", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
