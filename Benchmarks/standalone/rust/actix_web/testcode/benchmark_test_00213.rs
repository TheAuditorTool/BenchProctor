// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00213")]
pub async fn benchmark_test_00213(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(xml_value.clone());
    let mut _rng = fastrand::Rng::new();
    let _token = _rng.u64(..);
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
