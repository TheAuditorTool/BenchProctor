// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00061")]
pub async fn benchmark_test_00061(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    crate::shared::set_cookie(&format!("session={}; HttpOnly; SameSite=Strict", field_value));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
