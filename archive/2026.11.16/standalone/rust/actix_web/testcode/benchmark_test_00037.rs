// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00037")]
pub async fn benchmark_test_00037(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let (payload, _origin) = (auth_header.clone(), "http");
    let data = payload;
    use md5::Digest;
    let _ = md5::Md5::digest(data.as_bytes());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
