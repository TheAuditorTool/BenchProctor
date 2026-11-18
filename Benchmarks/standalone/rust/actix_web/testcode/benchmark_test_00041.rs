// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00041")]
pub async fn benchmark_test_00041(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let (payload, _origin) = (cookie_value.clone(), "http");
    let data = payload;
    use md5::Digest;
    let _ = md5::Md5::digest(data.as_bytes());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
