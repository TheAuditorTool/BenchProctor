// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use rand::rngs::OsRng;

#[actix_web::post("/benchmark_test_00474")]
pub async fn benchmark_test_00474(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let transform = |v: String| v.trim().to_string();
    let data = transform(field_value.clone());
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
