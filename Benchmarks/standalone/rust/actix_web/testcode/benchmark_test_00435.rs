// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use rand::rngs::OsRng;

#[actix_web::post("/benchmark_test_00435")]
pub async fn benchmark_test_00435(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut data = String::new();
    for token in ua_value.split(',') { data = token.to_string(); }
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
