// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00487")]
pub async fn benchmark_test_00487(req: HttpRequest) -> HttpResponse {
    let origin_value = req.headers().get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let (payload, _origin) = (origin_value.clone(), "http");
    let data = payload;
    use md5::Digest;
    let _ = md5::Md5::digest(data.as_bytes());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
