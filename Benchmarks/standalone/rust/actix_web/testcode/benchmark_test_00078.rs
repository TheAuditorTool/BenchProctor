// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00078")]
pub async fn benchmark_test_00078(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = header_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    let requested: u32 = data.parse().unwrap_or(0);
    let count = (requested * 4096) as usize;
    let _buf: Vec<u8> = vec![0u8; count];
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
