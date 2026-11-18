// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00050")]
pub async fn benchmark_test_00050(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    struct FormData { payload: String }
    let data = FormData { payload: field_value.clone() }.payload;
    crate::shared::set_cookie(&format!("session={}; Secure; HttpOnly; SameSite=Strict", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
