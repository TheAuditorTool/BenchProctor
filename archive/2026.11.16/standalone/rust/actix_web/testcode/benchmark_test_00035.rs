// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00035")]
pub async fn benchmark_test_00035(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let mut data = String::new();
    for token in field_value.split(',') { data = token.to_string(); }
    crate::shared::xpath_eval(&format!("//user[@id='{}']", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
