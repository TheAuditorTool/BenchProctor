// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00267")]
pub async fn benchmark_test_00267(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    struct FormData { payload: String }
    let data = FormData { payload: field_value.clone() }.payload;
    let Some(at) = data.find('@') else { return HttpResponse::BadRequest().finish(); };
    let mail_domain = &data[at + 1..];
    let _ = mail_domain;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
