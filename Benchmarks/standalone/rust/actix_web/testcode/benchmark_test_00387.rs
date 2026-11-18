// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use rand::rngs::OsRng;

#[actix_web::post("/benchmark_test_00387")]
pub async fn benchmark_test_00387(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(cookie_value.clone());
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
