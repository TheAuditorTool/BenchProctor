// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00015")]
pub async fn benchmark_test_00015(req: HttpRequest) -> HttpResponse {
    let forwarded_ip = req.headers().get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = forwarded_ip.to_string();
    let requested: u32 = data.parse().unwrap_or(0);
    let count = (requested * 4096) as usize;
    let _buf: Vec<u8> = vec![0u8; count];
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
