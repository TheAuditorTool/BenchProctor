// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00230")]
pub async fn benchmark_test_00230(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let mut data = String::new();
    for token in field_value.split(',') { data = token.to_string(); }
    let _chunk = web::Bytes::from(format!("<div>{}</div>", data));
    let mut _response = HttpResponse::Ok();
    _response.content_type("text/html; charset=utf-8");
    return _response.streaming(futures_util::stream::once(async move { Ok::<_, std::convert::Infallible>(_chunk) }));
}
