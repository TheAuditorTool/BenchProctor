// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use rand::rngs::SysRng;

#[actix_web::post("/benchmark_test_00185")]
pub async fn benchmark_test_00185(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    use rand::Rng;
    let mut _rng: rand::rngs::StdRng = rand::make_rng();
    let _token = _rng.next_u64();
    crate::shared::store_session(&format!("csrf_token:{}", field_value), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
