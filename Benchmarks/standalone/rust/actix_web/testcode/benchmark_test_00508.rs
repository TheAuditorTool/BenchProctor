// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00508")]
pub async fn benchmark_test_00508(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let captured = field_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let processed = html_escape::encode_text(&data).to_string();
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", processed));
}
