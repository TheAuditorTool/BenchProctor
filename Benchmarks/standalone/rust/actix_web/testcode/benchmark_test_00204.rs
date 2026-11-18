// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00204")]
pub async fn benchmark_test_00204(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let data: String = field_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| field_value.clone());
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
