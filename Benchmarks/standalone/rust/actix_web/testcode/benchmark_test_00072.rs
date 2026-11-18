// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00072")]
pub async fn benchmark_test_00072(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let (payload, _origin) = (field_value.clone(), "http");
    let data = payload;
    use md5::Digest;
    let _ = md5::Md5::digest(data.as_bytes());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
