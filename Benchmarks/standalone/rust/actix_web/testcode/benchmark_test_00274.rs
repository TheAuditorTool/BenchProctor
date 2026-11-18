// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00274")]
pub async fn benchmark_test_00274(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let data = match field_value.chars().next() { Some(_) => field_value.clone(), None => "default".to_string() };
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
