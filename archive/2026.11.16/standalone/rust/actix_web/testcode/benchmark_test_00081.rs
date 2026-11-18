// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00081")]
pub async fn benchmark_test_00081(req: HttpRequest) -> HttpResponse {
    let host_value = req.headers().get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", host_value).ok();
    use md5::Digest;
    let _ = md5::Md5::digest(data.as_bytes());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
