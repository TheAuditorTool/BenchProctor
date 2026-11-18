// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00578")]
pub async fn benchmark_test_00578(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let data = match field_value.chars().next() { Some(_) => field_value.clone(), None => "default".to_string() };
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", data));
}
