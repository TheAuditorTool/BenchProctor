// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00049")]
pub async fn benchmark_test_00049(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let transform = |v: String| v.trim().to_string();
    let data = transform(field_value.clone());
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
